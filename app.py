import os
from flask import Flask
from flask import render_template
from flask import request

# from flask_sqlalchemy import SQLAlchemy 
# import sqlalchemy as db

# engine = db.create_engine('mysql://root:miazocool1503@localhost/crud')
# connection = engine.connect()
# metadata = db.MetaData()
# census = db.Table('student', metadata, autoload=True, autoload_with=engine)

# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file

# db = SQLAlchemy(app)

# class Book(db.Model):
#     title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

#     def __repr__(self):
#         return "<Title: {}>".format(self.title)

@app.route("/", methods=["GET", "POST"])
def home():
#     if request.form:
#         print(request.form)  
    return render_template("index.html")
    #return "Hello World Kih"

@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route("/questionaire", methods=["GET","POST"])
def questionaire():
    return render_template("questionaire.html")

if __name__ == "__main__":
    app.run(debug=True)
    app.config['DEBUG']=True