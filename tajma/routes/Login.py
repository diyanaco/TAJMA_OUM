# from tajma import login_manager, app
from tajma import  app
from models import User, session
from tajma.forms import LoginForm
from flask import redirect, flash, url_for, render_template, Blueprint
from flask_principal import identity_loaded, RoleNeed, UserNeed
from flask_security import current_user

login_page = Blueprint('login', __name__,
                        template_folder='templates',
                        url_prefix='/login')

#Assign user roles
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Set the identity user object
    identity.user = current_user 
    print(f'identity is : {identity}')
    try:
        # Add the UserNeed to the identity
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Assuming the User model has a list of roles, update the
        # identity with the roles that the user provides
        if hasattr(current_user, 'roles'):
            for role in identity.user.roles:
                identity.provides.add(RoleNeed(role.code))

    except Exception as e:
        print("EXCEPTION : on_identity_loaded : " + str(e))

@login_page.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    login = form.check_login()
    if form.validate_on_submit():
        if login == True:
            return redirect(url_for('dashboard.dashboard'))
        elif login == False:
            flash("Your credentials are wrong")
        elif form.check_registered() == False:
            flash("Your email is not registered, please register first")
        else:
            flash("You are not elligible to login or register, please consult with OUM")
    return render_template("login.html", form=form)