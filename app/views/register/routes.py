from flask import Blueprint, render_template, url_for, redirect, request
from app.views.user.models import User
from app.extensions import db
from werkzeug.security import generate_password_hash

module = Blueprint("register", __name__, url_prefix="/register")


@module.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # get form data from request
        form = dict(request.form)
        form["password"] = generate_password_hash(form["password"])

        # add form data to database
        user = User(**form)
        db.session.add(user)
        db.session.commit()

        # redirect to login page
        return redirect(url_for("auth.index"))

    # render register page
    return render_template("pages/register.html")
