import tempfile

from flask import Flask, request, send_file

application = Flask(__name__)


@application.route("/hello")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@application.route("/")
def root():
    return open("pages/index.html", "r").read()


@application.route("/polygon2mbtiles", methods=["POST"])
def polygon2mbtiles():
    polygon_filestorage = request.files["polygon"]  # type: FileStorage

    with tempfile.NamedTemporaryFile("w+b") as polygon_tempfile:
        polygon_filestorage.save(polygon_tempfile)
        polygon_tempfile.seek(0)
        return send_file(polygon_tempfile.name, mimetype="image/jpg")


if __name__ == "__main__":
    application.run(host="0.0.0.0")
