from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, SelectField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from wtforms.fields.html5 import TimeField


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class CalendarAvailabilityForm(FlaskForm):
    # days = SelectMultipleField(
    #     'days', choices=[
    #         ("Monday", "monday"),
    #         ("Tuesday", "tuesday"),
    #         ("Wednesday", " wednesday"),
    #         ("Thursday", "thursday"),
    #         ("Friday", "friday")],
    #     validators=[DataRequired()])
    days = MultiCheckboxField('days',
                              choices=[
                                  ("Monday", "monday"),
                                  ("Tuesday", "tuesday"),
                                  ("Wednesday", " wednesday"),
                                  ("Thursday", "thursday"),
                                  ("Friday", "friday")], coerce=int,
                              validators=[DataRequired()])

    session_start = TimeField("Start", format='%H:%M')
    session_end = TimeField("End", format='%H:%M')
    submit = SubmitField('Add')
