from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
from pathlib import Path
import time
import time
import os.path


app = Flask(__name__)


def get_max_file(path_string: str):
    folder_path = Path(path_string)
    files = list(folder_path.glob("*.png"))
    return max(files, key=os.path.getctime)


def gen(path_string: str):
    max_file = get_max_file(path_string)

    while True:
        time.sleep(5)
        curr_max_file = get_max_file(path_string)
        if max_file != curr_max_file:
            print(f"OLD: {max_file} --- NEW: {curr_max_file}")

            im = open(curr_max_file, "rb").read()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + im + b"\r\n")
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + im + b"\r\n")
            max_file = curr_max_file

        print("Do nothing")


@app.route("/")
def test():
    return Response(gen("/mnt/flask"), mimetype="multipart/x-mixed-replace; boundary=frame")
    # return Response(gen(r"C:\Users\Andreas\Pictures\flask"), mimetype="multipart/x-mixed-replace; boundary=frame")


# @app.route("/")
# def index():
#     return "<html><head></head><body><h1>slideshow</h1><img src='/slideshow' style='width: 90%; height: 90%;'/>" "</body></html>"


if __name__ == "__main__":
    # app.run(threaded=True)
    app.run()
