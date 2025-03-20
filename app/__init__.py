from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register routes (we'll add this later)
    from app.routes.games import games_bp
    app.register_blueprint(games_bp)

    return app