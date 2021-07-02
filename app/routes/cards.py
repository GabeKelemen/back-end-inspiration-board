import functools
from flask import Blueprint, request, jsonify, make_response
from werkzeug.exceptions import NotFound
from app import db
from ..models.card import Card


bp = Blueprint('cards', __name__, url_prefix='/cards')

def require_card(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        card_id = kwargs.pop("card_id")
        card = Card.get(card_id)
        if not card:
            raise NotFound(dict(details=f"card id [{card_id}] not found"))

        kwargs["card"] = card

        return func(*args, **kwargs)

    return wrapper

@bp.route("<card_id>/upvote", methods=("PATCH",))
@require_card
def upvote(card):
    card.upvote()

    db.session.commit()

    return jsonify(card.to_dict()), 200


@bp.route("<card_id>", methods=("DELETE",))
@require_card
def delete(card):
    card.delete()

    db.session.commit()

    return jsonify(dict(details=f"deleted card id [{card.id}]")), 200
