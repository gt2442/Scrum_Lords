from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db
from .routes import main_routes, oauth
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Set secret key for sessions
    app.config['SECRET_KEY'] = os.getenv("GOOGLE_CLIENT_SECRET")

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///app.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Initialize OAuth
    oauth.init_app(app)

    # Register blueprints
    app.register_blueprint(main_routes)

    return app
