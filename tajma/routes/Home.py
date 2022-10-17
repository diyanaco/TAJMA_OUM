from flask import Blueprint,render_template

home_page = Blueprint('home', __name__,
                        template_folder='templates')
                        
@home_page.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")