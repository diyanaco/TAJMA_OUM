from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField

class SearchForm(FlaskForm):
    selectfield = SelectField('Type', choices=[('id', 'User ID'), ('firstName', 'First Name'), ('email','Email')])
    searchfield = StringField('Search')
    search = SubmitField('Search')