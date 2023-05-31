from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = "users.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("AUDIOWAVE_SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from website.views.public.start import start_bp
    from website.views.public.auth import auth_bp

    app.register_blueprint(start_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/')

    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            create_database()

    return app


def create_database():
    db.create_all()