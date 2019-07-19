from flask import request, jsonify
import json

from foo import app
from foo.user.userctrl import UserCtrl

@app.route('/', methods=['GET'])
def handle_default():
    return 'Online'

@app.route('/users', methods=['POST'])
def handle_user():
    data = json.loads(request.get_data().decode('utf-8'))
    ret = UserCtrl.add_user(data)
    return jsonify(ret)

@app.route('/countusers', methods=['POST'])
def handle_count_users():
    data = json.loads(request.get_data().decode('utf-8'))
    ret=UserCtrl.count_user(data)
    return jsonify(ret)
