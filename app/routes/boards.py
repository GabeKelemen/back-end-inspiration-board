import functools
from flask import Blueprint, request, jsonify, make_response
from werkzeug.exceptions import BadRequest, NotFound
from app import db
from ..models.board import Board
from ..models.card import Card

bp = Blueprint('boards', __name__, url_prefix='/boards')

def make_board_from_dict(data):
    required_fields = ["title", "owner"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise BadRequest(dict(details=f"missing fields: {', '.join(missing_fields)}"))

    return Board(**data)

def make_card_from_dict(data, board):
    required_fields = ["message"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise BadRequest(dict(details=f"missing fields: {', '.join(missing_fields)}"))

    return Card(board_id=board.id, **data)

def require_board(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        board_id = kwargs.pop("board_id")
        board = Board.get(board_id)
        if not board:
            raise NotFound(dict(details=f"board id [{board_id}] not found"))

        kwargs["board"] = board

        return func(*args, **kwargs)

    return wrapper

@bp.route("/", methods=("GET",))
def get_boards():
    return jsonify([board.to_dict() for board in Board.all()]), 200

@bp.route("/", methods=("POST",))
def create_board():
    request_body = request.get_json()
    if not request_body:
        raise BadRequest(dict(details="missing required data"))

    board = make_board_from_dict(request_body)

    db.session.add(board)
    db.session.commit()

    return jsonify(board.to_dict()), 201

@bp.route("/<board_id>/cards", methods=("GET",))
@require_board
def get_board_cards(board):
    sort_by = request.args.get('sort')
    return jsonify([card.to_dict() for card in board.cards_sorted(sort_by)]), 200

@bp.route("/<board_id>/cards", methods=("POST",))
@require_board
def create_card(board):
    request_body = request.get_json()
    if not request_body:
        raise BadRequest(dict(details="missing required data"))

    card = make_card_from_dict(request_body, board)

    db.session.add(card)
    db.session.commit()

    return jsonify(card.to_dict()), 201
