#Veify if user admin or not
from tajma import engine, app
from sqlalchemy.orm import sessionmaker
from tajma.model import db_insert_data, db_update_data
from tajma.model.UserModel import User
from flask_login import current_user, login_required
import secrets
import os
from PIL import Image
from flask import render_template, request, url_for, redirect

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

def isAdmin():
    userAdmin = session.query(User.id).filter(User.email == current_user.get_email()).scalar()
    if userAdmin.roles and userAdmin.roles[0].name == 'Admin':
        return True
    else:
        return False

#Save picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/assets/img/profile_pics', picture_fn)
    # resize the image
    output_size = (300, 300)
    i = Image.core.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn