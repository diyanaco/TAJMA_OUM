from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required, current_user
from tajma.forms import ElearningAnswer, AttitudeAnswer, LearnerAnswer
from tajma.models import *
import numpy as np
import uuid

psychometric_test_page = Blueprint('test', __name__,
                        template_folder='templates',
                        url_prefix='/test')

@psychometric_test_page.route("/elearning", methods=["GET","POST"])
@login_required
def elearning():
    form = ElearningAnswer()
    if form.validate_on_submit():
        #Kemahiran belajar
        trait1 = [form.answer1.data, form.answer2.data,
                  form.answer3.data, form.answer4.data,
                  form.answer5.data, form.answer6.data,
                  form.answer7.data, form.answer8.data,
                  form.answer9.data]
        #Kemahiran literasi
        trait2 = [form.answer10.data, form.answer11.data,
                  form.answer12.data, form.answer13.data,
                  form.answer14.data, form.answer15.data,
                  form.answer16.data, form.answer17.data,
                  form.answer18.data, form.answer19.data,
                  form.answer20.data, form.answer21.data]
        # Kemahiran hidup
        trait3 = [form.answer22.data, form.answer23.data,
            form.answer24.data, form.answer25.data,
            form.answer26.data, form.answer27.data,
            form.answer28.data, form.answer29.data,
            form.answer30.data]

        trait1 = round(np.mean(list(map(int, trait1))), 2)
        trait2 = round(np.mean(list(map(int, trait2))),2)
        trait3 = round(np.mean(list(map(int, trait3))), 2)

        result = Elearning(id=str(uuid.uuid4()), kb = trait1, kl=trait2, kh=trait3, userID=current_user.get_id())
        db_insert_data(result)
        user : User = session.query(User).filter(User.id == current_user.get_id()).scalar()
        user.elearningTaken = True
        db_update_data()
        return redirect(url_for("test.attitude"))
    return render_template("tp1Elearning.html", form=form)

@psychometric_test_page.route("/attitude", methods=["GET", "POST"])
@login_required
def attitude():
    form = AttitudeAnswer()
    if form.validate_on_submit():
        #Motivasi
        trait1 = [form.answer1.data, form.answer2.data,
                  form.answer3.data, form.answer4.data,
                  form.answer5.data, form.answer6.data,
                  form.answer7.data]
        #Keterbukaan          
        trait2 = [form.answer8.data, form.answer9.data,
                    form.answer10.data, form.answer11.data,
                    form.answer12.data, form.answer13.data,
                    form.answer14.data, form.answer15.data]
        #Kestabilan emosi
        trait3 = [form.answer16.data, form.answer17.data,
                  form.answer18.data, form.answer19.data,
                  form.answer20.data, form.answer21.data,
                  form.answer22.data]

        trait1 = round(np.mean(list(map(int, trait1))), 2)
        trait2 = round(np.mean(list(map(int, trait2))), 2)
        trait3 = round(np.mean(list(map(int, trait3))), 2)

        result = Attitude(id=str(uuid.uuid4()), ke=trait3,kt=trait2, mt=trait1, userID=current_user.get_id())
        db_insert_data(result)
        # Update the user table where test is taken 
        user : User = session.query(User.id).filter(User.id == current_user.get_id()).scalar()
        user.attitudeTaken = True
        db_update_data()
        return redirect(url_for("test.learner"))
    return render_template("tp2Attitude.html", form=form)

@psychometric_test_page.route("/learner", methods=["GET", "POST"])
@login_required
def learner():
    form = LearnerAnswer()
    if form.validate_on_submit():
        trait1 = [form.answer1.data, form.answer2.data,
            form.answer3.data, form.answer4.data,
            form.answer5.data, form.answer6.data,
            form.answer7.data]
        trait1 = round(np.mean(list(map(int, trait1))), 2)
        result = Learner(id=str(uuid.uuid4()), tr1=trait1, userID=current_user.get_id())
        db_insert_data(result)
        user = User.query.filter_by(id = current_user.get_id()).update(dict(learnerTaken = True))
        #Update the user table where test is taken 
        user : User = session.query(User.id).filter(User.id == current_user.get_id()).scalar()
        user.learnerTaken = True
        db_update_data()
        return redirect(url_for("success"))
    return render_template("tp3Learner.html", form=form)