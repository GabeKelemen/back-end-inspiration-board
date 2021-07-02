from app import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String, nullable=False)
    like_count = db.Column(db.Integer, nullable=False, server_default="0")
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'),
        nullable=False)

    def upvote(self):
        self.like_count += 1

    def delete(self):
        db.session.delete(self)

    def to_dict(self):
        return dict(
            id=self.id,
            message=self.message,
            like_count=self.like_count,
            board_id=self.board_id
        )

    @classmethod
    def get(cls, id):
        try:
            return cls.query.get(id)
        except ValueError:
            return None
