from flask import Blueprint, render_template,  jsonify, url_for, request, redirect

from tajma.forms.CreateCalendarEventForm import CalendarEventForm

calendar_page = Blueprint('calendar', __name__,
                        template_folder='templates',
                        url_prefix='/calendar')

@calendar_page.route('/', methods=["GET", "POST"])
def calendar():
    form = CalendarEventForm()
    form.errors
    if form.validate_on_submit():
        form.updateCalEvent()
        return redirect(url_for('calendar.calendar'))
    else :
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                error = err
    return render_template('FullCalendarEvents.html', form=form)

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
        resp = jsonify({'success' : 1, 'result' : rows})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@calendar_page.route('/google', methods=["GET", "POST"])
def google_calendar():
    return render_template('GoogleCalendar.html')