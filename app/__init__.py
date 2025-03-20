from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions (e.g., Flask-SQLAlchemy)
    from app.models.game import db
    db.init_app(app)

    # Register blueprints
    from app.routes.games import games_bp
    from app.routes.auth import auth_bp
    app.register_blueprint(games_bp)
    app.register_blueprint(auth_bp)

    return app