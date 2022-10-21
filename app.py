from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pathlib import Path
import base64
from io import BytesIO
from matplotlib.figure import Figure
import os

app = Flask(__name__)
# p = Path("/mnt")
# L = [x for x in p.iterdir() if x.is_dir()]


# @app.route("/")
# def hello():
#     # Generate the figure **without using pyplot**.
#     fig = Figure()
#     ax = fig.subplots()
#     ax.plot([1, 2])
#     # Save it to a temporary buffer.
#     buf = BytesIO()
#     fig.savefig(buf, format="png")
#     # Embed the result in the html output.
#     data = base64.b64encode(buf.getbuffer()).decode("ascii")
#     return f"<img src='data:image/png;base64,{data}'/>"
# @app.route("/")
# def index():
#     return "Flask app"


# @app.route("/")
# def index():
#     print("Request for index page received")
#     return render_template("index.html")


@app.route("/")
def favicon():
    return send_from_directory("/mnt/flask", "GitHub-Mark-64px.png")


# @app.route("/hello", methods=["POST"])
# def hello():
#     name = request.form.get("name")

#     if name:
#         print(f"{Path.cwd()}")
#         return render_template("hello.html", name=name)
#     else:
#         print("Request for hello page received with no name or blank name -- redirecting")
#         return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
