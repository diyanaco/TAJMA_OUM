from flask import Blueprint, render_template

google_sign_up_page = Blueprint('google-sign-up', __name__,
                       template_folder='templates',
                       url_prefix='/google-sign-up')


@google_sign_up_page.route('/', methods=["GET", "POST"])
def admin():
    return render_template("GoogleSignUp.html")