from .Admin import admin_page
from .Dashboard import dashboard_page

def init_app(app):
    app.register_blueprint(admin_page)
    app.register_blueprint(dashboard_page)    

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