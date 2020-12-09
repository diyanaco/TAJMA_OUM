from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SECRET_KEY'] = '1d66b518598641b6d88a3f0115780daf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tajma.db'
db = SQLAlchemy(app)

from tajma import routes