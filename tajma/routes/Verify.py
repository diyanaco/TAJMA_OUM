from tajma.forms import VerificationForm
from flask import flash, session as localSession, redirect, url_for, Blueprint, render_template

verify_page = Blueprint('verify', __name__,
                        template_folder='templates',
                        url_prefix='/verify')

@verify_page.route("/", methods=["GET", "POST"])
def verify():
    form = VerificationForm()
    if form.validate_on_submit():
        if form.check_email() == True:
            flash(
                'A confirmation email has been sent, please verify first, then continue with the registration')
            localSession["email"] = form.email.data
            return redirect(url_for('register.register'))
        else:
            flash('You are not elligible to register, please verify with OUM', 'success')
    return render_template("verify.html", form=form)