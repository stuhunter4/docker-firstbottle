import bottle
from bottle import route


def success():
    app = bottle.default_app()

    @route('/')
    def home():
        return "<h2>Success!</h2>"

    return app
