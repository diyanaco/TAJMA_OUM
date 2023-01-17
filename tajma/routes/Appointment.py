from flask import Blueprint, render_template,  jsonify, url_for, request, redirect
from tajma.forms.CreateCalendarEventForm import CalendarEventForm
from models import *
from datetime import datetime, timedelta
from tajma.FlaskPrincipalPermission import student_permission
appointment_page = Blueprint('appointment', __name__,
                          template_folder='templates',
                          url_prefix='/appointment')


@appointment_page.route('/', methods=["GET", "POST"])
@student_permission.require(http_exception=403)
def appointment():
    form = CalendarEventForm()
    # Upon submitting the form
    if form.validate_on_submit():
        form.updateCalEvent()
        return redirect(url_for('dashboard.dashboard'))
    return render_template('Appointment.html', form=form)
