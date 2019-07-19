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

    @staticmethod
    def count_user(data):
        try:
            target_iq = int(data['target_iq'])
            result_users = User.query.filter(User.user_iq >= target_iq).all()
            result_users_names = []
            for u in result_users:
                result_users_names.append(u.user_name)
            return {
                'code': 0,
                'msg': 'success',
                'data': result_users_names
            }
        except Exception as e:
            db.session.rollback()
            return {
                'code': -1,
                'msg': 'error',
                'data': ''
            }