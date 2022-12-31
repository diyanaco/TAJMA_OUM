from flask_wtf import FlaskForm 
from flask_wtf.file import FileAllowed
from wtforms import FileField, SubmitField

class UpdateProfileForm(FlaskForm):
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    #email = StringField('Email', validators=[DataRequired(), Email()])
    update = SubmitField('Update')
