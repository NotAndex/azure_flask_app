from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
from pathlib import Path
import time
from io import BytesIO
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirCreatedEvent, FileCreatedEvent

app = Flask(__name__)


class CustomHandler(FileSystemEventHandler):
    """Custom handler for Watchdog"""

    def __init__(self):
        # List to store path
        self.path_strings = []

    # callback for File/Directory created event, called by Observer.
    def on_created(self, event: FileCreatedEvent):

        self.path_strings.append(Path(event.src_path).as_posix())

        print(f"Path content: \n{self.path_strings}")


def main():
    # get current path as absolute, linux-style path.
    working_path = Path("/mnt/flask").as_posix()
    # working_path = Path(r"C:\Users\Andreas\Pictures\GitHub-Mark\PNG").as_posix()

    # create instance of observer and CustomHandler
    observer = Observer()
    handler = CustomHandler()

    # start observer, checks files recursively
    observer.schedule(handler, path=working_path, recursive=False)
    observer.start()
    print("observer started")

    try:
        while True:
            time.sleep(1)
            print(f"Image to yield == {len(handler.path_strings)} Time: {datetime.now()}")
            if len(handler.path_strings):
                im = open(handler.path_strings.pop(), "rb").read()
                print(f"After read {handler.path_strings}")
                # for i in range(2):  # IDK why this double yield is needed
                #     print(f"loop: {i}")
                yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + im + b"\r\n")
                yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + im + b"\r\n")
            else:
                im = open("/mnt/flask/inception.png", "rb").read()
                # for i in range(2):  # IDK why this double yield is needed
                #     print(f"loop: {i}")
                yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + im + b"\r\n")
                yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + im + b"\r\n")

    except KeyboardInterrupt:
        observer.stop()
    observer.join()


@app.route("/slideshow")
def slideshow():

    return Response(main(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/")
def index():
    return "<html><head></head><body><h1>slideshow</h1><img src='/slideshow' style='width: 90%; height: 90%;'/>" "</body></html>"


if __name__ == "__main__":
    # app.run(threaded=True)
    app.run()
