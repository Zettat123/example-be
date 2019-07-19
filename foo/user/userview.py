from flask import request, jsonify
import json

from foo import app
from foo.user.userctrl import UserCtrl


@app.route('/users', methods=['POST'])
def handle_user():
    data = json.loads(request.get_data().decode('utf-8'))
    ret = UserCtrl.add_user(data)
    return jsonify(ret)
