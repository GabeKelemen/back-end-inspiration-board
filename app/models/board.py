from app import db
from .card import Card

sort_columns = {
    "message-asc": (Card.message, Card.id),
    "message-desc": (Card.message.desc(), Card.id),
    "likes-asc": (Card.like_count, Card.id),
    "likes-desc": (Card.like_count.desc(), Card.id),
}

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)
    cards = db.relationship('Card', backref='board', lazy="dynamic")

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            owner=self.owner,
        )

    def cards_sorted(self, sort_by):
        sort_column = sort_columns.get(sort_by, (Card.id,))

        return self.cards.order_by(*sort_column)

    @classmethod
    def all(cls):
        return cls.query.order_by(Board.id).all()

    @classmethod
    def get(cls, id):
        try:
            return cls.query.get(id)
        except ValueError:
            return None