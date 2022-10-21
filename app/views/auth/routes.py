from flask import Blueprint, render_template, url_for, redirect, flash, request, session
from app.views.user.models import User
from werkzeug.security import check_password_hash

module = Blueprint("auth", __name__, url_prefix="/auth")


@module.route("/login", methods=["GET", "POST"])
def index():
    # in POST request, if email and password are correct, redirect to user page
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect(url_for("user.index"))

        flash("User not found")

    # if user id in session, redirect to user page
    user_id = session.get("user_id")
    if user_id:
        return redirect(url_for("user.index"))

    # render login page
    return render_template("pages/login.html")


@module.route("/logout")
def logout():
    # remove user id in session and redirect to login page
    session.pop("user_id", None)

    return redirect(url_for("auth.index"))
