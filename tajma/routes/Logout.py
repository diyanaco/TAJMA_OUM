from flask import Blueprint, redirect, url_for
from flask_login import login_required, logout_user
logout_page = Blueprint('logout', __name__,
                        template_folder='templates',
                        url_prefix='/logout')

@logout_page.route("/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))