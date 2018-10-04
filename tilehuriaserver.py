import tempfile

from flask import Flask, request, send_file

from tilehuria.polygon2mbtiles import main

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
    name_pieces = polygon_filestorage.filename.split(".")
    if len(name_pieces) <= 1:
        return "Could not determine file extension. " + polygon_filestorage.filename
    else:
        extension = "." + name_pieces[-1]

    with tempfile.NamedTemporaryFile("w+b", suffix=extension) as polygon_tempfile:
        polygon_filestorage.save(polygon_tempfile)
        polygon_tempfile.seek(0)
        opts = {
            "infile": polygon_tempfile.name,
            "minzoom": 16,
            "maxzoom": 20,
            "tileserver": "digital_globe_standard",
            "format": "JPEG",
            "colorspace": "YCBCR",
            "type": "baselayer",
            "description": "A tileset",
            "attribution": "Copyright of the tile provider",
            "version": "1.0",
        }
        main(opts)
        tiledir = opts["tiledir"]
        filename = tiledir + ".mbtiles"
        return send_file(filename, mimetype="application/vnd.mapbox-vector-tile")


if __name__ == "__main__":
    application.run(host="0.0.0.0")
