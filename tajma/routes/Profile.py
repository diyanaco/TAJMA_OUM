from flask import Blueprint, request, url_for, render_template, jsonify, make_response
from flask_login import login_required, current_user
from models import *
from tajma.constants import RoleEnum
from tajma.forms import CalendarAvailabilityForm, UpdateProfileForm
import uuid
from operator import add
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
    slots: Slot = session.query(Slot).filter(
        Slot.counselor_id == current_user.get_id()).all()
    slots_deserialized = [
        {
            "days": ', '.join(days_deserializers(x.days)),
            "start_slot": x.start_slot,
            "end_slot": x.end_slot
        }
        for x in slots]

    return render_template("profile.html", prof=prof,
                           profile_form=profile_form,
                           availability_form=availability_form,
                           slots=slots_deserialized)


@profile_page.route("/create-slot", methods=["POST"])
def create_slot():
    req = request.get_json()
    days_serialized = days_serializers(req["selected_days"])

    slot = Slot(id=str(uuid.uuid4()), start_slot=req["slot_start"],
                end_slot=req["slot_end"], days=days_serialized)
    db_insert_data(slot)
    slots = session.query(Slot).filter(
        Slot.counselor_id == current_user.get_id()).all()
    slots_deserialized = [
        {
            "days": ', '.join(days_deserializers(x.days)),
            "start_slot": x.start_slot,
            "end_slot": x.end_slot
        }
        for x in slots]
    res = make_response(jsonify(slots_deserialized), 200)
    return res
    

def days_deserializers(days):
    days_deserialized = []
    for index, day in enumerate(days):
        if(day=="1" and index==0):
            days_deserialized.append("Monday")
        if(day=="1" and index==1):
            days_deserialized.append("Tuesday")
        if(day=="1" and index==2):
            days_deserialized.append("Wednesday")
        if(day=="1" and index==3):
            days_deserialized.append("Thursday")
        if(day=="1" and index==4):
            days_deserialized.append("Friday")
        if(day=="1" and index==5):
            days_deserialized.append("Saturday")
        if(day=="1" and index==6):
            days_deserialized.append("Sunday")
    return days_deserialized

def days_serializers(days):
    day_serialized = [0,0,0,0,0,0,0]
    for day in days:
        if day == 'Monday':
            day_serialized = list( map (add, day_serialized, [1,0,0,0,0,0,0]))        
        if day == 'Tuesday':
            day_serialized = list( map (add, day_serialized, [0,1,0,0,0,0,0]))
        if day == 'Wednesday':
            day_serialized = list( map (add, day_serialized, [0,0,1,0,0,0,0]))
        if day == 'Thursday':
            day_serialized = list( map (add, day_serialized, [0,0,0,1,0,0,0]))
        if day == 'Friday':
            day_serialized = list( map (add, day_serialized, [0,0,0,0,1,0,0]))
        if day == 'Saturday':
            day_serialized = list( map (add, day_serialized, [0,0,0,0,0,1,0]))
        if day == 'Sunday':
            day_serialized += list( map (add, day_serialized, [0,0,0,0,0,0,1]))
    return day_serialized