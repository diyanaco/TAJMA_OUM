
from flask_login import current_user, login_user
from flask import redirect, url_for, session as localSession, Blueprint, render_template
from tajma.forms import RegistrationForm
register_page = Blueprint('register', __name__,
                        template_folder='templates',
                        url_prefix='/register')

@register_page.route("/", methods=["GET", "POST"])
def register():
    #reroute the user to dashboard if its already sign in
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))
    form = RegistrationForm()
    fn, ln, gender, age, IC, race, mobile = form.retrieve_data()
    if form.validate_on_submit():
        #check credentials then insert data
        form.check_credentials()
        #issue4 temporary used only, the assignment of role will be done front end by superAdmin
        #after normal user register, will route to the main dashboard
        #superAdmin will then assign them admin role later after registration
        #after that, the user with admin role will route to admin page after login
        if localSession.get("email") == "admin@demo.com":
            form.assign_admin()
            return redirect(url_for('admin.admin'))
        #ISSUE 3 create function first time login
        #flash("Succesfully Register, please login")
        return redirect(url_for('dashboard.dashboard'))
    return render_template("register.html", form=form, fn=fn, ln=ln, em=localSession.get("email"))
