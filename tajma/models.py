from tajma import db
#from __init__ import db


class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=True)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    profPic = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"User('{self.email}', '{self.password}')"

#inserting data
if not User.query.all():
    user_1 = User(userID='01', firstName='Zaim', lastName='Saha', email='zaim@demo.com', password='password')
    user_2 = User(userID='02', firstName='Joyce', lastName='Yong', email='joyce@demo.com', password='password')
    db.session.add(user_1)
    db.session.add(user_2)
    db.session.commit()

class Student(db.Model):
    studentID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=True)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    profPic = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Student('{self.email}', '{self.firstName}')"

#inserting data
if not Student.query.all():
    student_1 = Student(studentID='01', firstName='Zaim', lastName='Saha', email='zaim@demo.com')
    student_2 = Student(studentID='02', firstName='Joyce', lastName='Yong', email='joyce@demo.com')
    student_3 = Student(studentID='03', firstName='Taufiq', lastName='Yusup', email='taufiq@demo.com')
    student_4 = Student(studentID='04', firstName='Haziq', lastName='Isma', email='haziq@demo.com')
    db.session.add(student_1)
    db.session.add(student_2)
    db.session.add(student_3)
    db.session.add(student_4)
    db.session.commit()

class Question(db.Model):
    instruCode = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(50), unique=True, nullable=False)
    label = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Question('{self.question}', '{self.code}')"


class Result(db.Model):
    resultID = db.Column(db.Integer(), primary_key=True, nullable=False)
    instruCode = db.Column(db.String(10), nullable=False)
    SB = db.Column(db.Float(), nullable=False)
    PM = db.Column(db.Float(), nullable=False)
    PT = db.Column(db.Float(), nullable=False)
    AN = db.Column(db.Float(), nullable=False)
    PN = db.Column(db.Float(), nullable=False)
    AS = db.Column(db.Float(), nullable=False)
    PN = db.Column(db.Float(), nullable=False)
    JD = db.Column(db.Float(), nullable=False)
    IG = db.Column(db.Float(), nullable=False)
    KP = db.Column(db.Float(), nullable=False)
    KD = db.Column(db.Float(), nullable=False)
    KS = db.Column(db.Float(), nullable=False)
    KC = db.Column(db.Float(), nullable=False)


class Code(db.Model):
    code = db.Column(db.Integer(), nullable=False, primary_key=True)
    desc = db.Column(db.String(50), nullable=False)
