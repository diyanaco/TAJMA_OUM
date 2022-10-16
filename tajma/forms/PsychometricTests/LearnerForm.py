from . import FieldsRequiredForm
from wtforms import RadioField, SubmitField

class LearnerAnswer(FieldsRequiredForm):
    #trait 1 
    answer1 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer2 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer3 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer4 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer5 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer6 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer7 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    submit = SubmitField("Submit")
