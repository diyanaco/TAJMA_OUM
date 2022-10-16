from . import FieldsRequiredForm
from wtforms import RadioField, SubmitField

class AttitudeAnswer(FieldsRequiredForm):
    #trait 1 Motivasi
    answer1 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer2 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer3 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer4 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer5 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer6 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer7 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)

    #trait 2 Keterbukaan
    answer8 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer9 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer10 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer11 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer12 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer13 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer14 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer15 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)

    #trait 3 Kestabilan emosi
    answer16 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer17 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer18 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer19 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer20 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer21 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    answer22 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)

    # #Trait 4 Keberkesanan Diri
    # answer23 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
    # answer24 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer25 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer26 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer27 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer28 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer29 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    
    # #Trait 5 Kebolehsuaian
    # answer30 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer31 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer32 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer33 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer34 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer35 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer36 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer37 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])

    # #Akauntabiliti/Kebertanggungjawab
    # answer38 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer39 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer40 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer41 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer42 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer43 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer44 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])

    # #Pengarahan diri
    # answer45 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer46 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer47 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer48 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer49 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer50 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])

    # #Silang budaya
    # answer51 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer52 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer53 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer54 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer55 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer56 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer57 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer58 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])

    # #Daya ketahanan
    # answer59 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer60 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer61 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer62 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer63 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer64 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer65 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    # answer66 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])

    submit = SubmitField("Submit")

