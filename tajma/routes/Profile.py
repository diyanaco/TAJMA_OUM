from flask import Blueprint, request, url_for, render_template
from flask_login import login_required, current_user
from models import *
from tajma.constants import RoleEnum
from tajma.forms import CalendarAvailabilityForm, UpdateProfileForm

profile_page = Blueprint('profile', __name__,
                         template_folder='templates',
                         url_prefix='/profile')


@profile_page.route("/", methods=["GET", "POST"])
@login_required
def profile():
    availability_form = CalendarAvailabilityForm()
    profile_form = UpdateProfileForm()
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
    return render_template("profile.html", prof=prof,
                           profile_form=profile_form,
                           availability_form=availability_form)
