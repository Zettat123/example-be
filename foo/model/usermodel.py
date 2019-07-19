from foo import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(10))
    user_iq = db.Column(db.Integer)

    def __init__(self, user_name, user_iq):
        self.user_name = user_name
        self.user_iq = user_iq

    def __repr__(self):
        return "<User %r>" % self.user_name
