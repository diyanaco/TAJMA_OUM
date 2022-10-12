
from tokenize import String
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from tajma.models import User, session
save_page = Blueprint('save', __name__,
                        template_folder='templates',
                        url_prefix='/save')

@save_page.route("/save/<test>", methods=["GET", "POST"])
@login_required
def save(test : String):
    try :
        print(test)
        if test == "elearner":
            user : User = session.query(User).filter(User.id == current_user.id).scalar()
            user.elearningTaken = True
        if test == "attitude":
            return render_template("saveProgress.html")
    except Exception as e :
        session.rollback()
        session.close()
        return (str(e))