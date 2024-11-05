from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db
from .routes import main_routes
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register routes
    app.register_blueprint(main_routes)

    return app
