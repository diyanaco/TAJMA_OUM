from . import FieldsRequiredForm
from wtforms import RadioField, SubmitField

class ElearningAnswer(FieldsRequiredForm):
    #trait 1 Kemahiran Belajar
    answer1 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer2 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer3 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer4 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer5 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer6 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer7 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer8 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer9 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)

    #trait 2 Kemahiran Literasi
    answer10 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer11 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer12 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer13 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer14 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer15 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer16 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer17 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer18 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer19 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer20 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer21 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)

    #trait 3 Kemahiran Hidup
    answer22 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer23 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer24 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer25 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer26 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer27 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer28 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer29 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer30 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)



    submit = SubmitField("Submit")
