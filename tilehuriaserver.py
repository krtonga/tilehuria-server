from flask import Flask

application = Flask(__name__)


@application.route("/hello")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@application.route("/")
def root():
    return open("pages/index.html", "r").read()


if __name__ == "__main__":
    application.run(host="0.0.0.0")
