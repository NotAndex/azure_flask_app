from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
from pathlib import Path
import time
import time
import os.path


app = Flask(__name__)


def gen(path_string: str):
    idx = 0

    while True:

        if idx == 0:
            im = open("/mnt/flask/inception.png", "rb").read()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + im + b"\r\n")
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + im + b"\r\n")
            idx += 1
        time.sleep(15)
        if idx == 1:
            im = open("/mnt/flask/adf_drawio.png", "rb").read()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + im + b"\r\n")
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + im + b"\r\n")
            idx -= 1


@app.route("/slideshow")
def slideshow():
    return Response(gen("/mnt/flask"), mimetype="multipart/x-mixed-replace; boundary=frame")
    # return Response(gen(r"C:\Users\Andreas\Pictures\flask"), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/")
def index():
    return "<html><head></head><body><h1>slideshow</h1><img src='/slideshow' style='width: 90%; height: 90%;'/>" "</body></html>"


if __name__ == "__main__":
    app.run(threaded=True)
    # app.run()
