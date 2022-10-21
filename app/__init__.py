from flask import Flask, redirect, url_for
from .views.auth.routes import module as auth
from .views.register.routes import module as register
from .views.user.routes import module as user
from .extensions import db, ma
from .commands import create_tables


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")

    # initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # register router
    app.register_blueprint(auth)
    app.register_blueprint(register)
    app.register_blueprint(user)

    # add flask command
    app.cli.add_command(create_tables)

    @app.errorhandler(404)
    def page_not_found(e):
        # note that we set the 404 status explicitly
        return redirect(url_for("auth.index"))

    return app
