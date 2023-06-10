from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from website.utils import install
from website.models.db import Audio
from website import db

home_bp = Blueprint("home_bp", __name__)

@home_bp.route("/home", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST" :
        url = request.form.get("url")

        audio_data = install.install(url)

        new_audio = Audio(title=audio_data[1], author=audio_data[2],
                          path=audio_data[0], user_id=current_user.id)
        
        db.session.add(new_audio)
        db.session.commit()

    return render_template("public/home.html")

