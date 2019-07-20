from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *

from .config import *
from foo.model import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+DB_USER+DB_PASSWORD+':@'+DB_HOST+':'+DB_PORT+'/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

CORS(app, supports_credentials=True)
db = SQLAlchemy(app=app)

import foo.router