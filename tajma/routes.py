from flask import render_template, url_for, flash, redirect, request, has_request_context, session
from tajma import app
from tajma.form import LoginForm, RegistrationForm, VerificationForm
from tajma.models import Question
from flask_login import current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        if form.check_credentialsLOGIN() == True:
            # next_page = request.args.get('next')
            # return redirect(next_page) if next_page else render_template('login.html'))
            return redirect(url_for('dashboard'))
        elif form.check_credentialsLOGIN() == False:
            flash("Your credentials are wrond")
        elif form.check_registered == False:
            flash ("Your email is not registered, please register first")
            #ISSUE 1 create a link to registration
        else :
            flash ("You are not elligible to login or register, please consult with OUM")
            #redirect to index.html
    return render_template("login.html", form=form)


# @app.route("/questionaire", methods=["GET", "POST"])
# def questionaire():
#     return render_template("questionaire.html", value=myresult)


@app.route("/verify", methods=["GET", "POST"])
def verify():
    form = VerificationForm()
    if form.validate_on_submit():
        if form.check_email() == True:
            flash('A confirmation email has been sent, please verify first, then continue with the registration')
            session["email"] = form.email.data
            return redirect(url_for('register'))
        else:
            flash('You are not elligible to register, please verify with OUM')
    return render_template("verify.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegistrationForm()
    fn, ln = form.retrieve_data()
    if form.validate_on_submit():
        form.check_credentials()
        #ISSUE 3 create function first time login
        #flash("Succesfully Register, please login")
        return redirect(url_for('dashboard'))
    return render_template("register.html", form=form, fn=fn, ln=ln, em=session.get("email") )

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    #if has_request_context():
    tpType = request.args.get('type')
    if tpType is None :
        return render_template("dashboard.html")
    elif tpType =='prof':
        prof ={
            "fullname" : "Taufiq Usup",
            "gender" : current_user.get_gender(),
            "age" : current_user.get_age(),
            "IC" : current_user.get_IC(),
            "race" : current_user.get_race(),
            "mobile" : current_user.get_mobile(),
            "email" : current_user.get_email(),
            "image" : url_for('static', filename='assets/img/profile_pics/' + current_user.profPic)
        }
        return render_template("dashboard.html", prof=prof)
    else:
        if tpType == '1':
            ques = Question.query.filter(Question.instruCode.like('01%')).all()
            title = "OUM Learners Personality Profile"
        if tpType == '2':
            ques = Question.query.filter(Question.instruCode.like('02%')).all()
            title = "E-Learning Styles"
        if tpType == '3':
            ques = Question.query.filter(Question.instruCode.like('03%')).all()
            title = "Life-long Learning Attitude"
        ques_value = [q.question for q in ques]
        return render_template("dashboard.html", value=ques_value, title=title)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))