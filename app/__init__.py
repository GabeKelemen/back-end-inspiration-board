from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_cors import CORS
from app.errors.handlers import BadRequest, NotFound

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI_TEST")

    db.init_app(app)
    migrate.init_app(app, db)

    # from app.models.board import Board
    # from app.models.card import Card

    from .routes import boards, cards
    app.register_blueprint(boards.bp)
    app.register_blueprint(cards.bp)

    CORS(app)

    BadRequest(app)
    NotFound(app)

    return app
