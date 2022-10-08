import routes
from flask_login import login_required, current_user

@routes.app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    print(f'current user is : {current_user}')
    testTaken = {
        "elearning" : routes.session.query(routes.User).filter(routes.User.id == current_user.get_id()).scalar().elearningTaken,
        "learner" : routes.session.query(routes.User).filter(routes.User.id == current_user.get_id()).scalar().learnerTaken,
        "attitude" : routes.session.query(routes.User).filter(routes.User.id == current_user.get_id()).scalar().attitudeTaken,
    }
    return routes.render_template("dashboard.html", testTaken=testTaken)