from flask_login import current_user
from .Admin import admin_page
from .Dashboard import dashboard_page
from .Home import home_page
from .Login import login_page
from .PsychometricTest import psychometric_test_page
from .Register import register_page
from .Verify import verify_page
from .Profile import profile_page
from .Calendar import calendar_page
from .Logout import logout_page
from .SaveProgress import save_page

def init_app(app):
    app.register_blueprint(home_page)   
    app.register_blueprint(login_page)   
    app.register_blueprint(register_page)   
    app.register_blueprint(admin_page)
    app.register_blueprint(dashboard_page)   
    app.register_blueprint(psychometric_test_page)   
    app.register_blueprint(verify_page)   
    app.register_blueprint(profile_page)
    app.register_blueprint(calendar_page)
    app.register_blueprint(logout_page)
    app.register_blueprint(save_page)


#Save picture
# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     # picture_path = os.path.join(
#     #     app.root_path, 'static/assets/img/profile_pics', picture_fn)
#     # resize the image
#     output_size = (300, 300)
#     i = Image.core.open(form_picture)
#     i.thumbnail(output_size)
#     # i.save(picture_path)
#     return picture_fn