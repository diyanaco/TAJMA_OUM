from tajma import app
# from werkzeug.exceptions import BadRequest
from flask import render_template
def handle_bad_request(e):
    message = "You Don't Have Permission "
    return render_template('ErrorPage.html', message=message), 403
