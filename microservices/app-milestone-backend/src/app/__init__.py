from flask import Flask
from app.infraestructure.mysql_database import DataBaseConfig
from app.infraestructure.system_logs import Logs
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import secrets
import importlib

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    """
    Create and configure a Flask application.

    Returns:
        app: The Flask application.
    """
    # Create the Flask application
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": "*"}})

    # Generate a secure secret key
    app.secret_key = secrets.token_urlsafe(32)

    # Configure the application with database settings
    app.config.from_object(DataBaseConfig)

    # Initialize the database within the application
    db.init_app(app)

    blueprints = [
        # (module, blueprint_object)
        ("app.application.question.question_controller", "question_bp"),
    ]

    for module_name, bp_name in blueprints:
        module = importlib.import_module(module_name)
        blueprint = getattr(module, bp_name)
        app.register_blueprint(blueprint)

    return app


with create_app().app_context():  # Crea un contexto de aplicación para que SQLAlchemy sepa a qué aplicación pertenece
    db.create_all()  # Crea las tablas en la base de datos si no existen
