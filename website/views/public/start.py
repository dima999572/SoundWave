from flask import Blueprint, render_template


start_bp = Blueprint("start_bp", __name__)

@start_bp.route("/", methods=["GET", "POST"])
def start():
    return render_template("public/start.html")