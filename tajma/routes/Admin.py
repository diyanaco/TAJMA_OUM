from models import *
from tajma.form import SearchForm
from flask import Blueprint, render_template, redirect, request, url_for
from random import randint
from flask_login import login_required, current_user
from flask_principal import Permission, RoleNeed
from tajma.constants import RoleEnum
from models import session
from tajma.FlaskPrincipalPermission import admin_permission

admin_page = Blueprint('admin', __name__,
                       template_folder='templates',
                       url_prefix='/admin')

# def isAdmin():
#     # userAdmin = session.query(User.id).filter(User.email == current_user.get_email()).scalar()
#     # if userAdmin.roles and userAdmin.roles[0].name == 'Admin':
#     #     return True
#     # else:
#     #     return False


@admin_page.route('/', methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def admin():
    # if isAdmin():
    form = SearchForm()
    if form.validate_on_submit():
        kwargs = {
            form.selectfield.data: form.searchfield.data
        }
        userSearch = User.query.filter_by(**kwargs).all()

        return render_template('admin.html', form=form, userSearch=userSearch)
    # need to fix this
    if request.args.get('type'):
        hello = "Hello"
        return render_template('admin.html', form=form, hello=hello)
    return render_template("admin.html", form=form)
    # else:
    #     return redirect(url_for('login'))

# View results


@admin_page.route("/results", methods=["GET"])
@login_required
def result_user():
    print(f"current_user is : {current_user}")
    elearning = session.query(Elearning).filter(
        Elearning.userID == current_user.get_id()).scalar()
    if elearning is None:
        message = "The user has not taken any test yet"
        return redirect(url_for('error', error=message))
    result1 = {
        "kb": round(elearning.kb/5*100, 1),
        "kh": round(elearning.kh/5*100, 1),
        "kl": round(elearning.kl/5*100, 1)
    }

    # Retrieve Learner result
    learner = session.query(Learner).filter_by(
        userID=current_user.get_id()).scalar()
    if learner is None:
        message = "The user has not taken any test yet"
        return redirect(url_for('error', error=message))
    result2 = {
        "trait1": round(learner.trait1/5*100, 1),
        "trait2": round(learner.trait2/5*100, 1),
        "trait3": round(learner.trait3/5*100, 1)
    }

    # Retrieve Attitude result
    attitude = session.query(Attitude).filter_by(
        userID=current_user.get_id()).scalar()
    if attitude is None:
        message = "The user has not taken any test yet"
        return redirect(url_for('error', error=message))
    result3 = {
        "trait1": round(attitude.trait1/5*100, 1),
        "trait2": round(attitude.trait2/5*100, 1),
        "trait3": round(attitude.trait3/5*100, 1)
    }
    # Merging dictionary
    result = {**result1, **result2, **result3}
    # Declare empty list
    labels = []
    values = []
    for k, v in result.items():
        labels.append(k)
        values.append(v)
    # get the user info
    labels = ["TR1", "TR2", "TR3", "TR4", "TR5",
              "TR6", "TR7", "TR8", "TR9", "TR10"]
    valuesIndividual = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(
        0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
    valuesMale = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(
        0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
    valuesFemale = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(
        0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]

    user = session.query(User).filter(
        User.id == current_user.get_id()).scalar()
    userProf = user.profPic
    print(f'user is : {user}')
    print(f'user profile is : {userProf}')

    return render_template('ResultUser.html', valuesIndividual=valuesIndividual, valuesMale=valuesMale, valuesFemale=valuesFemale, labels=labels, result=result, userProf=userProf)


@admin_page.route("/results/<id>", methods=["GET"])
@login_required
def results_admin(id):
    print(f"current_user is : {current_user}")
    if isAdmin():
        elearning = Elearning.query.filter_by(userID=id).first()
        if elearning is None:
            message = "The user has not taken any test yet"
            return redirect(url_for('error', error=message))
        result = {
            "kb": round(elearning.kb/5*100, 1),
            "kh": round(elearning.kh/5*100, 1),
            "kl": round(elearning.kl/5*100, 1)
        }
        labels = ["TR1", "TR2", "TR3", "TR4", "TR5",
                  "TR6", "TR7", "TR8", "TR9", "TR10"]
        valuesIndividual = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(
            0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
        valuesMale = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(
            0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
        valuesFemale = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(
            0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]

        userProf = User.query.filter_by(id=current_user.get_id()).first()
        return render_template('ResultAdmin.html', valuesIndividual=valuesIndividual, valuesMale=valuesMale, valuesFemale=valuesFemale, labels=labels, result=result, userProf=userProf)
    else:
        return redirect(url_for('login'))
