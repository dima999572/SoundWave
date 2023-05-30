from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("AUDIOWAVE_SECRET_KEY")

    from website.views.public.start import start_bp
    from website.views.public.auth import auth_bp

    app.register_blueprint(start_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/')

    return app