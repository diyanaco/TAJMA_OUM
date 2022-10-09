from flask import Blueprint, request, url_for, render_template
from tajma.form import UpdateAccountForm
from flask_login import login_required, current_user
profile_page = Blueprint('profile', __name__,
                        template_folder='templates',
                        url_prefix='/login')


@profile_page.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    tpType = request.args.get('type')
    prof = {
        "fullname": current_user.get_first_name() + " " + current_user.get_last_name(),
        "gender": current_user.get_gender(),
        "age": current_user.get_age(),
        "IC": current_user.get_IC(),
        "race": current_user.get_race(),
        "mobile": current_user.get_mobile(),
        "email": current_user.get_email(),
        "image": url_for('static', filename='assets/img/profile_pics/' + current_user.profPic)
    }
    # if tpType == 'mod':
    #     form = UpdateAccountForm()
    #     if form.validate_on_submit():
    #         if form.picture.data:
    #             picture_data = save_picture(form.picture.data)
    #             current_user.profPic = picture_data
    #             db.session.commit()
    #             flash('Your account has been updated', 'success')
    #             return redirect(url_for('profile', type='prof'))
    #     return render_template("profile.html", prof=prof, form=form)
    return render_template("profile.html", prof=prof)   