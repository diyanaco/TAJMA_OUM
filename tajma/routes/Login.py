import routes
from tajma.form import LoginForm
from flask import redirect, flash, url_for

@routes.app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.check_credentialsLOGIN() == True:
            if form.check_role() == "Admin":
                return redirect(url_for('admin'))
            else :
                return redirect(url_for('dashboard'))
        elif form.check_credentialsLOGIN() == False:
            flash("Your credentials are wrong")
        elif form.check_registered == False:
            flash("Your email is not registered, please register first")
        else:
            flash("You are not elligible to login or register, please consult with OUM")
    return routes.render_template("login.html", form=form)