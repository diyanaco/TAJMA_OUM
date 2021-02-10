import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, has_request_context, session
from sqlalchemy.orm import relation
from tajma import app, db
from tajma.form import ElearningAnswer, LoginForm, RegistrationForm, SearchForm, VerificationForm, UpdateAccountForm, SearchForm
from tajma.models import User, Elearning, db_insert_data, db_update_data
from flask_login import current_user, logout_user, login_required
import numpy as np
from random import randint

#Veify if user admin or not
def isAdmin():
    userAdmin = User.query.filter_by(email = current_user.get_email()).first()
    if userAdmin.roles and userAdmin.roles[0].name == 'Admin':
        return True
    else:
        return False

#Save picture
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

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    testTaken = {
        "elearning" : User.query.filter_by(id = current_user.get_id()).first().elearningTaken,
        "learner" : User.query.filter_by(id = current_user.get_id()).first().learnerTaken,
        "attitude" : User.query.filter_by(id = current_user.get_id()).first().attitudeTaken
    }
    return render_template("dashboard.html", testTaken=testTaken)

@app.route('/admin', methods=["GET", "POST"])
def admin():
    if isAdmin():
        form = SearchForm()
        if form.validate_on_submit():
            kwargs = {
                form.selectfield.data : form.searchfield.data
            }
            userSearch = User.query.filter_by(**kwargs).all()
            
            return render_template('admin.html', form=form, userSearch=userSearch)
        #need to fix this
        if request.args.get('type') :
                hello = "Hello"
                return render_template('admin.html', form= form, hello=hello)
        return render_template("admin.html", form=form)
    else :
        return redirect(url_for('login'))

#View results
@app.route("/admin/results/<id>", methods=["GET"])
@login_required
def results(id):
    if isAdmin():
        #Retrieve elearning result
        elearning = Elearning.query.filter_by(userID=id).first()
        if elearning is None:
            message="The user has not taken any test yet"
            return redirect(url_for('error', error=message))
        result = {
            "kb" : round(elearning.kb/5*100, 1),
            "kh" : round(elearning.kh/5*100, 1),
            "kl" : round(elearning.kl/5*100, 1)
        }

        # #Retrieve Learner result
        # learner = Learner.query.filter_by(userID=id).first()
        # if learner is None:
        #     message="The user has not taken any test yet"
        #     return redirect(url_for('error', error=message))
        # result2 = {
        #     "trait1" : round(learner.trait1/5*100, 1),
        #     "trait2" : round(learner.trait2/5*100, 1),
        #     "trait3" : round(learner.trait3/5*100, 1)
        # }

        # #Retrieve Attitude result
        # attitude = Attitude.query.filter_by(userID=id).first()
        # if attitude is None:
        #     message="The user has not taken any test yet"
        #     return redirect(url_for('error', error=message))
        # result3 = {
        #     "trait1" : round(attitude.trait1/5*100, 1),
        #     "trait2" : round(attitude.trait2/5*100, 1),
        #     "trait3" : round(attitude.trait3/5*100, 1)
        # }
        # #Merging dictionary
        # result={**result1,**result2,**result3}
        # #Declare empty list
        # labels= []
        # values=[]
        # for k,v in result.items():
        #     labels.append(k)
        #     values.append(v)
        #get the user info
        labels=["TR1", "TR2", "TR3", "TR4", "TR5", "TR6", "TR7", "TR8", "TR9", "TR10"]
        valuesIndividual=[randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100)]
        valuesGroup=[randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100)]
        
        userProf = User.query.filter_by(id=id).first()
        #fn = request.args.get('fn')
        # return render_template('results.html',values=values, labels=labels,result=result, 
        #                         result1=result1,result2=result2,result3=result3, userProf=userProf)
        return render_template('results.html',valuesIndividual=valuesIndividual,valuesGroup=valuesGroup, labels=labels,result=result,userProf=userProf)
 
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

@app.route("/elearning", methods=["GET","POST"])
@login_required
def elearning():
    form = ElearningAnswer()
    if form.validate_on_submit():
        trait1 = [form.answer1.data, form.answer2.data,
                  form.answer3.data, form.answer4.data,
                  form.answer5.data, form.answer6.data,
                  form.answer7.data, form.answer8.data,
                  form.answer9.data]

        trait2 = [form.answer10.data, form.answer11.data,
                  form.answer12.data, form.answer13.data,
                  form.answer14.data, form.answer15.data,
                  form.answer16.data, form.answer17.data,
                  form.answer18.data, form.answer19.data,
                  form.answer20.data, form.answer21.data]

        trait3 = [form.answer22.data, form.answer23.data,
            form.answer24.data, form.answer25.data,
            form.answer26.data, form.answer27.data,
            form.answer28.data, form.answer29.data,
            form.answer30.data]

        trait1 = round(np.mean(list(map(int, trait1))), 2)
        trait2 = round(np.mean(list(map(int, trait2))),2)
        trait3 = round(np.mean(list(map(int, trait3))), 2)

        result = Elearning(kb = trait1, kl=trait2, kh=trait3, userID=current_user.get_id())
        db_insert_data(result)
        user = User.query.filter_by(id = current_user.get_id()).update(dict(elearningTaken = True))
        #Update the user table where test is taken 
        db_update_data()
        return redirect(url_for("attitude"))
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

@app.route("/error/M/<error>")
def error(error):
    return render_template('error.html', error=error)
