from app import db
from .card import Card

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

    def cards_sorted(self):
        return self.cards.order_by(Card.id)

    @classmethod
    def all(cls):
        return cls.query.order_by(Board.id).all()

    @classmethod
    def get(cls, id):
        try:
            return cls.query.get(id)
        except ValueError:
            return None