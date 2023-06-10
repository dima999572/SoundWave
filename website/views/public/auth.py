from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.models.db import User
from website import db
from flask_login import login_user, logout_user


auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash("Logged in successfully!")
                login_user(user, remember=True)
                return redirect(url_for("home_bp.home"))
            else:
                flash("Incorrect password, try again.")
        else:
            flash("Email does not exist, try again.")

    return render_template("public/login.html")

@auth_bp.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))

@auth_bp.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exist.")
        elif len(firstName) < 2:
            flash("First name must be greater than 1 character.")
        elif len(lastName) < 2:
            flash("Last name must be greater than 1 character.")
        elif len(email) < 7:
            flash("Email must be greater than 7 characters.")
        elif password1 != password2:
            flash("Passwords don't match.")
        elif len(password1) < 8:
            flash("Password must be greater than 7 characters.")
        else:
            print(firstName)
            new_user = User(firstName=firstName, lastName=lastName, email=email, password=password1)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("auth_bp.login"))

    return render_template("public/sign_up.html")