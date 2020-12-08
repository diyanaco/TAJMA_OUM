import os
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 
#import sqlalchemy as db
import mysql.connector
from flask_debugtoolbar import DebugToolbarExtension
from login import LoginForm

app = Flask(__name__)

###Database config
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="miazocool1503",
#   database="tajma",
#   #auth_plugin='mysql_native_password'
# )

# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM ques")
# myresult = mycursor.fetchall()

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'zaim'
# toolbar = DebugToolbarExtension(app)

#sqlalchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tajma.db'
db = SQLAlchemy(app)

class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=True )
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    profPic = db.Column(db.String(20), nullable=False, default = 'default.jpg')
    
    def __repr__(self):
       return f"User('{self.email}', '{self.password}')"

class Question(db.Model):
    instruCode = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(50), unique=True, nullable=False)
    label = db.Column(db.String(10), nullable=False)

    def __repr__(self):
      return f"Question('{self.question}', '{self.code}')"

class Result(db.Model):
    resultID = db.Column(db.Integer(), primary_key=True, nullable=False)
    instruCode = db.Column(db.String(10), nullable=False)
    SB = db.Column(db.Float(), nullable=False)
    PM = db.Column(db.Float(), nullable=False)
    PT = db.Column(db.Float(), nullable=False)
    AN = db.Column(db.Float(), nullable=False)
    PN = db.Column(db.Float(), nullable=False)
    AS = db.Column(db.Float(), nullable=False)
    PN = db.Column(db.Float(), nullable=False)
    JD = db.Column(db.Float(), nullable=False)
    IG = db.Column(db.Float(), nullable=False)
    KP = db.Column(db.Float(), nullable=False)
    KD = db.Column(db.Float(), nullable=False)
    KS = db.Column(db.Float(), nullable=False)
    KC = db.Column(db.Float(), nullable=False)
    
class Code(db.Model):
    code = db.Column(db.Integer(), nullable=False, primary_key=True)
    desc = db.Column(db.String(50), nullable=False)

@app.route("/", methods=["GET", "POST"])
def home():
#     if request.form:
#         print(request.form)  
    return render_template("index.html")
    #return "Hello World Kih"

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data =='password':
            flash('You have been logged in', 'success')
            return render_template('dashboard.html')
    return render_template("login.html", form=form)

@app.route("/questionaire", methods=["GET","POST"])
def questionaire():
    return render_template("questionaire.html", value=myresult)

@app.route("/test", methods=["GET","POST"])
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)
    app.config['DEBUG']=True