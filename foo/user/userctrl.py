from foo import db
from foo.model.usermodel import User


class UserCtrl:
    @staticmethod
    def add_user(data):
        try:
            p = User(data['user_name'], data['user_iq'])
            db.session.add(p)
            db.session.commit()
            return {
                'code': 0,
                'msg': 'success',
                'data': ''
            }
        except Exception as e:
            db.session.rollback()
            return {
                'code': -1,
                'msg': 'error',
                'data': ''
            }
