import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, has_request_context, session
from tajma import app, db
from tajma.form import Elearning, LoginForm, RegistrationForm, VerificationForm, UpdateAccountForm, AnswerElearningTrait3Form, AnswerElearningTrait2Form, AnswerElearningTrait1Form
from tajma.models import User
from flask_login import current_user, logout_user, login_required
import numpy as np

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        if form.check_credentialsLOGIN() == True:
            # next_page = request.args.get('next')
            # return redirect(next_page) if next_page else render_template('login.html'))
            if form.check_role() == "Admin":
                return redirect(url_for('admin'))
            else :
                return redirect(url_for('dashboard'))
        elif form.check_credentialsLOGIN() == False:
            flash("Your credentials are wrong")
        elif form.check_registered == False:
            flash("Your email is not registered, please register first")
            # ISSUE 1 create a link to registration
        else:
            flash("You are not elligible to login or register, please consult with OUM")
            # redirect to index.html
    return render_template("login.html", form=form)

@app.route("/verify", methods=["GET", "POST"])
def verify():
    form = VerificationForm()
    if form.validate_on_submit():
        if form.check_email() == True:
            flash(
                'A confirmation email has been sent, please verify first, then continue with the registration')
            session["email"] = form.email.data
            return redirect(url_for('register'))
        else:
            flash('You are not elligible to register, please verify with OUM', 'success')
    return render_template("verify.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    #reroute the user to dashboard if its already sign in
    # if current_user.is_authenticated:
    #     return redirect(url_for('dashboard'))
    form = RegistrationForm()
    fn, ln, gender, age, IC, race, mobile = form.retrieve_data()
    if form.validate_on_submit():
        #check credentials then insert data
        form.check_credentials()
        #issue4 temporary used only, the assignment of role will be done front end by superAdmin
        #after normal user register, will route to the main dashboard
        #superAdmin will then assign them admin role later after registration
        #after that, the user with admin role will route to admin page after login
        if session.get("email") == "admin@demo.com":
            form.assign_admin()
            return redirect(url_for('admin'))
        #ISSUE 3 create function first time login
        #flash("Succesfully Register, please login")
        return redirect(url_for('dashboard'))
    return render_template("register.html", form=form, fn=fn, ln=ln, em=session.get("email"))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/assets/img/profile_pics', picture_fn)
    # resize the image
    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    welcome = True
    return render_template("dashboard.html", value=welcome)

@app.route('/admin')
def admin():
    user = User.query.filter_by(email = current_user.get_email()).first()
    if user.roles and user.roles[0].name == 'Admin':
            return render_template("admin.html")
    else :
            return redirect(url_for('login'))

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    tpType = request.args.get('type')
    prof = {
        "fullname": current_user.get_first_name() + " " + current_user.get_last_name(),
        "gender": current_user.get_gender(),
        "age": current_user.get_age(),
        "IC": current_user.get_IC(),
        "race": current_user.get_race(),
        "mobile": current_user.get_mobile(),
        "email": current_user.get_email(),
        "image": url_for('static', filename='assets/img/profile_pics/' + current_user.profPic)
    }
    if tpType == 'mod':
        form = UpdateAccountForm()
        if form.validate_on_submit():
            if form.picture.data:
                picture_data = save_picture(form.picture.data)
                current_user.profPic = picture_data
                db.session.commit()
                flash('Your account has been updated', 'success')
                return redirect(url_for('profile', type='prof'))
        return render_template("profile.html", prof=prof, form=form)
    return render_template("profile.html", prof=prof)        

@app.route("/elearning")
@login_required
def elearning():
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
    return render_template("tpElearning.html", form=form)

@app.route("/attitude")
@login_required
def attitude():
    return render_template("tpAttitude.html")

@app.route("/learner")
@login_required
def learner():
    return render_template("tpLearner.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
