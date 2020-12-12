from flask import render_template, url_for, flash, redirect
from tajma import app
from tajma.login import LoginForm
from tajma.register import RegistrationForm
from tajma.models import Question

# Temporary question
# myresult = [(1, 'Hello'), (2, 'Hehe'), (3, 'Hello'),
#             (4, 'Hehe'), (5, 'Hello'), (6, 'Hehe')]


@app.route("/", methods=["GET", "POST"])
def home():
    #     if request.form:
    #         print(request.form)
    return render_template("index.html")
    # return "Hello World Kih"


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.check() == True:
            return render_template('dashboard.html')
        else:
            flash("You are not registered, please register first")
    return render_template("login.html", form=form)


# @app.route("/questionaire", methods=["GET", "POST"])
# def questionaire():
#     return render_template("questionaire.html", value=myresult)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.check() == True:
            flash(
                'A confirmation email has been sent, please verify first, then continue with the registration')
        else:
            flash('You are not elligible to register, please verify with OUM')
    return render_template("register.html", form=form)

@app.route("/attitude", methods=["GET", "POST"])
def attitude():
    ques = Question.query.filter(Question.instruCode.like('01%')).all()
    ques_value = [q.question for q in ques]
    return render_template("tpAttitude.html", value=ques_value)

@app.route("/learner", methods=["GET", "POST"])
def learner():
    ques = Question.query.filter(Question.instruCode.like('02%')).all()
    ques_value = [q.question for q in ques]
    return render_template("tpLearner.html",value=ques_value)

@app.route("/elearning", methods=["GET", "POST"])
def elearning():
    ques = Question.query.filter(Question.instruCode.like('03%')).all()
    ques_value = [q.question for q in ques]
    return render_template("tpElearning.html", value=ques_value)