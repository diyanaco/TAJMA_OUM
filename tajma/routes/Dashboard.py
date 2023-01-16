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
@admin_permission.require(http_exception=403)
@login_required
def dashboard():
    print(f'current user is : {current_user}')
    #Retrieve user information
    user: User = session.query(User).filter(
        User.id == current_user.get_id()).scalar()
    testTaken = {
        "elearning": user.elearningTaken,
        "learner": user.learnerTaken,
        "attitude": user.attitudeTaken,
    }
    #Check if user is admin
    isAdmin = session.query(User).join(association_user_role_table).join(
        Role).filter(Role.code == RoleEnum.ADMIN.value, User.id == current_user.get_id()).all()
    # TODO #19 Research why db and fe not sync
    # Upon changing the data in the db, the data is not reflected immediately in fe after first refresh
    # but the data is reflected after several refresh.
    # Edited :
    #   Can test within the system whether the update is in sync. After one test, then route back to dashboard
    #   to see the test taken being in effect or not
    print(f'test taken is : {testTaken}')
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
    # TODO #19 Research why db and fe not sync
    # Upon changing the data in the db, the data is not reflected immediately in fe after first refresh
    # but the data is reflected after several refresh.
    # Edited :
    #   Can test within the system whether the update is in sync. After one test, then route back to dashboard
    #   to see the test taken being in effect or not
    print(f'test taken is : {test}')
    flash(f'Your {test} progress has been saved')
    return render_template("dashboard.html", testTaken=testTaken)
