from flask import Blueprint, render_template, url_for, redirect, request, session
from app.views.user.models import User, UserSchema
from app.extensions import db

module = Blueprint("user", __name__)


def get_user_by_id(id):
    user = User.query.get(id)
    return UserSchema().dump(user)


@module.route("/", methods=["GET"])
def index():
    # redirect to login page if there is no user id in session
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("auth.index"))

    # render user profile page
    user = get_user_by_id(user_id)
    return render_template("pages/profile.html", user=user, editable=True)


@module.route("/update", methods=["PATCH"])
def update():
    user_id = session.get("user_id")

    # update user data
    User.query.filter_by(id=user_id).update(dict(request.form))
    db.session.commit()

    # query updated user data
    user = get_user_by_id(user_id)
    return {"message": "User successfully updated", "data": user}


@module.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    session.pop("user_id", None)

    # delete user
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

    return {"message": "User successfully deleted"}


@module.route("/users", methods=["GET"])
def users():
    users = User.query.all()
    return render_template("pages/users.html", users=users)


@module.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = get_user_by_id(id)
    return render_template("pages/profile.html", user=user, editable=False)
