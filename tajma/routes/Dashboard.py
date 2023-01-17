# from flask_login import login_required, current_user
from flask import Blueprint, render_template, flash
from models import *
from flask_principal import Permission, RoleNeed
from tajma.constants import RoleEnum
from tajma.FlaskPrincipalPermission import user_permission, admin_permission
from flask_security import current_user, login_required
dashboard_page = Blueprint('dashboard', __name__,
                           template_folder='templates',
                           url_prefix='/dashboard')


@dashboard_page.route("/", methods=["GET", "POST"])
@user_permission.require(http_exception=403)
@login_required
def dashboard():
    # Retrieve user information
    user: User = session.query(User).filter(
        User.id == current_user.get_id()).scalar()
    testTaken = {
        "elearning": user.elearningTaken,
        "learner": user.learnerTaken,
        "attitude": user.attitudeTaken,
    }
    isAdmin = session.query(User).join(association_user_role_table).join(
        Role).filter(Role.code == RoleEnum.ADMIN.value, User.id == current_user.get_id()).all()
    return render_template("dashboard.html", testTaken=testTaken, adminView=isAdmin)


@dashboard_page.route("/query/<test>", methods=["GET", "POST"])
@admin_permission.require()
@login_required
def dashboardWithFlash(test):
    print(f'current user is : {current_user}')
    print(f'Inside dashboard(testTaken)')
    user: User = session.query(User).filter(
        User.id == current_user.get_id()).scalar()
    testTaken = {
        "elearning": user.elearningTaken,
        "learner": user.learnerTaken,
        "attitude": user.attitudeTaken,
    }
    flash(f'Your {test} progress has been saved')
    return render_template("dashboard.html", testTaken=testTaken)
