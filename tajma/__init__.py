from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '1d66b518598641b6d88a3f0115780daf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tajma.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from tajma import routes