from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from foo.model import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1:3306/example'

db = SQLAlchemy(app=app)

import foo.router