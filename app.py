import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy 
import sqlalchemy as db
import mysql.connector
from flask_debugtoolbar import DebugToolbarExtension

#Database config
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="miazocool1503",
  database="tajma",
  #auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM ques")
myresult = mycursor.fetchall()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zaim'
toolbar = DebugToolbarExtension(app)

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
    hello = "Hello"
    return render_template("questionaire-me.html", value=myresult , hello=hello)

@app.route("/test", methods=["GET","POST"])
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)
    app.config['DEBUG']=True