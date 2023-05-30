from flask import Blueprint, render_template, request, redirect, url_for


auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template("public/login.html")

@auth_bp.route("/logout", methods=["GET", "POST"])
def logout():
    return redirect(url_for("auth_bp.login"))

@auth_bp.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("public/sign_up.html")