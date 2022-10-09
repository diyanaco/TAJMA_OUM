from flask import Blueprint, render_template,  jsonify

calendar_page = Blueprint('calendar', __name__,
                        template_folder='templates',
                        url_prefix='/calendar')

@calendar_page.route('/')
def calendar():
    return render_template('FullCalendar.html')

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
                        "title": "Event 1",
                        "url": "http://example.com",
                        "class": "event-important",
                        "start": 12039485678000, 
                        "end": 1234576967000 
                    },
                    {
                        "id": 103,
                        "title": "Event 1",
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