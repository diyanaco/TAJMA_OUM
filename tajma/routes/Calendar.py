from flask import Blueprint, render_template,  jsonify, url_for, request, redirect
from tajma.forms.CreateCalendarEventForm import CalendarEventForm
from tajma.models import *

calendar_page = Blueprint('calendar', __name__,
                          template_folder='templates',
                          url_prefix='/calendar')


@calendar_page.route('/', methods=["GET", "POST"])
def calendar():
    form = CalendarEventForm()
    form.errors
    # Upon submitting the form
    if form.validate_on_submit():
        form.updateCalEvent()
        return redirect(url_for('calendar.calendar'))
    else:
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                error = err
    # If got events
    # Getting events
    calendarEvents = session.query(CalendarEvent).all()
    events = []
    # Mapping of events
    for event in calendarEvents:
        events.append({
            "id": event.id,
            # "allDay": ,
            "start": calculateStart(event.appointment_date, event.slot),
            #End date maybe redundant, sin
            "end": calculateEnd(event.appointment_date, event.slot),
            "title": event.title,
            # String. A URL that will be visited when this event is clicked by the user.
            # For more information on controlling this behavior, see the eventClick callback.
            # "url",
            "editable" : True,
            "backgroundColor" : "rgb(252,186,3)",
            "textColor":"rgb(227, 223, 213)",
            # A plain object holding miscellaneous other properties specified during parsing. 
            # Receives properties in the explicitly given extendedProps hash as well as other 
            # non-standard properties.
            "extendedProps":{
                "slot": event.slot,
                "participants": getParticipants(),
                "summary": event.summary
            }
        })
    # events = [
    #     {
    # ]
    return render_template('FullCalendarEvents.html', form=form, events=events)


@calendar_page.route('/calendar-events')
def calendar_events():
    conn = None
    cursor = None
    try:
        rows = [
            {
                "id": 101,
                "title": "Event 1",
                "url": "http://example.com",
                "class": "event-important",
                "start": 12039485678000,
                "end": 1234576967000
            },
            {
                "id": 102,
                "title": "Event 2",
                "url": "http://example.com",
                "class": "event-important",
                "start": 12039485678000,
                "end": 1234576967000
            },
            {
                "id": 103,
                "title": "Event 3",
                "url": "http://example.com",
                "class": "event-important",
                "start": 12039485678000,
                "end": 1234576967000
            }
        ]
        resp = jsonify({'success': 1, 'result': rows})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@calendar_page.route('/google', methods=["GET", "POST"])
def google_calendar():
    return render_template('GoogleCalendar.html')

def getParticipants():
    """Get list of participants from link table

    Returns:
        list: list of participants
    """
    return str("Participants")

def calculateEnd(startDate, slot):
    return str(startDate)

def calculateStart(startDate, slot):
    return str(startDate) 

def generateTitle(slot):
    return str(slot)
