import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, has_request_context, session
from tajma import app, db
from tajma.form import Elearning, LoginForm, RegistrationForm, VerificationForm, UpdateAccountForm, AnswerElearningTrait3Form, AnswerElearningTrait2Form, AnswerElearningTrait1Form
from tajma.models import Question, Result
from flask_login import current_user, logout_user, login_required
import numpy as np

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
            flash('You are not elligible to register, please verify with OUM', 'success')
    return render_template("verify.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegistrationForm()
    fn, ln, gender, age, IC, race, mobile = form.retrieve_data()
    if form.validate_on_submit():
        form.check_credentials()
        #ISSUE 3 create function first time login
        #flash("Succesfully Register, please login")
        return redirect(url_for('dashboard'))
    return render_template("register.html", form=form, fn=fn, ln=ln, em=session.get("email") )

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/assets/img/profile_pics', picture_fn)
    #resize the image
    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    #if has_request_context():
    tpType = request.args.get('type')
    prof ={
            "fullname" : current_user.get_first_name() +" "+ current_user.get_last_name(),
            "gender" : current_user.get_gender(),
            "age" : current_user.get_age(),
            "IC" : current_user.get_IC(),
            "race" : current_user.get_race(),
            "mobile" : current_user.get_mobile(),
            "email" : current_user.get_email(),
            "image" : url_for('static', filename='assets/img/profile_pics/' + current_user.profPic)
        }
    if tpType is None :
        return render_template("dashboard.html")
        
    elif tpType =='prof':
        return render_template("dashboard.html", prof=prof)

    elif tpType=='mod':
        form=UpdateAccountForm()
        if form.validate_on_submit():
            if form.picture.data:
                picture_data = save_picture(form.picture.data)
                current_user.profPic = picture_data
                db.session.commit()
                flash('Your account has been updated', 'success')
                return redirect(url_for('dashboard', type='prof'))
        return render_template("dashboard.html", prof=prof, form=form)
    elif tpType=='wel':
        wel = ''
        return render_template("dashboard.html", welcome=wel)
    else:
        form = Elearning()
        if form.validate_on_submit():
            trait1 = [form.answer1.data, form.answer2.data,
                    form.answer3.data, form.answer4.data,
                    form.answer5.data, form.answer6.data,
                    form.answer7.data, form.answer8.data,
                    form.answer9.data]
            trait1 = np.mean(trait1)

            trait2 = [form.answer10.data, form.answer11.data,
                    form.answer12.data, form.answer13.data,
                    form.answer14.data, form.answer15.data,
                    form.answer16.data, form.answer17.data,
                    form.answer18.data, form.answer19.data,
                    form.answer20.data, form.answer21.data]
            trait2 = np.mean(trait2)

        #for i in range(form.answer)
        if request.method == 'POST':
            answer = request.form.getlist('answer')
            #answer = form.answer.data
        if tpType == '1':
            ques = Question.query.filter(Question.instruCode.like('01%')).all()
            title = "OUM Learners Personality Profile"
        elif tpType == '2':
            ques = Question.query.filter(Question.instruCode.like('02%')).all()
            title = "E-Learning Styles"
        elif tpType == '3':
            ques = Question.query.filter(Question.instruCode.like('03%')).all()
            title = "Life-long Learning Attitude"
        else :
            ques =[]
            title =""
        ques_value = [q.question for q in ques]
        return render_template("dashboard.html", value=ques_value,form=form, title=title)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))