from flask_login import login_required, current_user
from flask import Blueprint, render_template
from tajma.models import *
from flask_principal import Permission, RoleNeed

admin_permission = Permission(RoleNeed('SUPER_ADMIN'))
dashboard_page = Blueprint('dashboard', __name__,
                        template_folder='templates',
                        url_prefix='/dashboard')

@dashboard_page.route("/", methods=["GET", "POST"])
@admin_permission.require()
@login_required
def dashboard():
    print(f'current user is : {current_user}')
    testTaken = {
        "elearning" : session.query(User).filter(User.id == current_user.get_id()).scalar().elearningTaken,
        "learner" : session.query(User).filter(User.id == current_user.get_id()).scalar().learnerTaken,
        "attitude" : session.query(User).filter(User.id == current_user.get_id()).scalar().attitudeTaken,
    }
    return render_template("dashboard.html", testTaken=testTaken)