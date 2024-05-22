from flask import Flask

from my_pkg import pages


def create_app() -> Flask:
    app = Flask(import_name=__name__)
    app.register_blueprint(blueprint=pages.bp)
    return app
