# # from tajma import db,login_manager
# from tajma import login_manager
# from flask_login import UserMixin
# from tajma import Base
# from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Float
# from sqlalchemy.orm import relationship, sessionmaker
# from tajma import engine

# # db.drop_all()
# Session = sessionmaker()
# Session.configure(bind=engine)
# session = Session()

# @login_manager.user_loader
# def load_user(user_id):
#     print(f'user is : {session.query(User).get(user_id)}')
#     return session.query(User).get(user_id)

# def db_insert_data(model):
#     session.add(model)
#     session.commit()

# def db_update_data():
#     session.commit()


# class User(Base, UserMixin):
#     __tablename__ = "psy_user"
#     id = Column(String(50), primary_key=True)
#     firstName = Column(String(50), nullable=True)
#     lastName = Column(String(50), nullable=False)
#     email = Column(String(50), unique=True, nullable=False)
#     password = Column(String(100), nullable=False)
#     gender = Column(String(50), nullable=False)
#     age = Column(String(50), nullable=False)
#     profPic = Column(String(50), nullable=False, default='default.jpg')
#     IC = Column(String(50), nullable=False)
#     race = Column(String(50), nullable=False)
#     mobile = Column(String(50), nullable=False)
#     # roles = relationship('Role', secondary='user_roles')
#     # active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
#     email_confirmed_at = Column(DateTime)
#     elearningTaken = Column(Boolean, nullable =True)
#     learnerTaken = Column(Boolean, nullable =True)
#     attitudeTaken = Column(Boolean, nullable =True)


#     #override get_id method from UserMixin
#     def get_id(self):
#         return self.id
#     def get_first_name(self):
#         return self.firstName
#     def get_last_name(self):
#         return self.lastName
#     def get_email(self):
#         return self.email
#     def get_gender(self):
#         return self.gender
#     def get_age(self):
#         return self.age
#     def get_profPic(self):
#         return self.profPic
#     def get_IC(self):
#         return self.IC
#     def get_race(self):
#         return self.race
#     def get_mobile(self):
#         return self.mobile

#     def __repr__(self):
#         return f"User('{self.email}', '{self.password}', {self.id})"

# class Role(Base):
#     __tablename__="psy_role"
#     id = Column(String(50), primary_key=True)
#     name = Column(String(50), unique=True)

# class UserRoles(Base):
#     __tablename__ = 'psy_user_roles'
#     id = Column(String(50), primary_key=True)
#     user_id = Column(String(50), ForeignKey('psy_user.id', ondelete='CASCADE'))
#     role_id = Column(String(50), ForeignKey('psy_role.id', ondelete='CASCADE'))

# #inserting data
# # if db.engine.dialect.has_table(db.engine, "user"):
# #     if not User.query.all():
# #if SQLAlchemy.inspect(db.engine).get_table_names():
# # user = User(id='03', firstName='Taufiq', lastName='Yusup', email='taufiq@demo.com', password='$2b$12$gtSd6v3IT3fZHk5OjY5cHergOjygyLujz.y0cFsWM/ppGF7CRezai', gender="MALE", age="22", IC="910321035515",race="Malay", mobile="0179163956")
# # session.add(user)
# # session.commit()

# # if not User.query.all():
# # user_1 = User(id='01', firstName='Zaim', lastName='Saha', email='zaim@demo.com', password='password')
# # user_2 = User(id='02', firstName='Joyce', lastName='Yong', email='joyce@demo.com', password='password')
# # session.add(user_1)
# # session.add(user_2)
# # session.commit()

# class Student(Base):
#     __tablename__ = "psy_student"
#     studentID = Column(String(50), primary_key=True)
#     firstName = Column(String(50), nullable=True)
#     lastName = Column(String(50), nullable=False)
#     email = Column(String(50), unique=True, nullable=False)
#     profPic = Column(String(50), nullable=False, default='default.jpg')
#     gender = Column(String(50), nullable=False)
#     age = Column(String(50), nullable=False)
#     IC = Column(String(50), nullable=False)
#     race = Column(String(50), nullable=False)
#     mobile = Column(String(50), nullable=False)

#     def __repr__(self):
#         return f"Student('{self.email}', '{self.firstName}')"

# #inserting data
# #if db.engine.dialect.has_table(db.engine, "student"):
# # # if db.inspect(db.engine).has_table("student"):
# # #     if not Student.query.all():
# # student_1 = Student(studentID='01', firstName='Zaim', lastName='Saha', email='zaim@demo.com', gender='Male', age='29', IC=910321035515, race='Malay', mobile= '0179163956')
# # student_2 = Student(studentID='02', firstName='Joyce', lastName='Yong', email='joyce@demo.com', gender='Female', age='28', IC=920315031234, race='Chinese', mobile= '01791678965')
# # student_3 = Student(studentID='03', firstName='Taufiq', lastName='Yusup', email='taufiq@demo.com', gender='Male', age='32', IC=9103610376515, race='Malay', mobile= '01791364956')
# # student_4 = Student(studentID='04', firstName='Haziq', lastName='Isma', email='haziq@demo.com',gender='Male', age='14', IC=910326375515, race='Malay', mobile= '0179097956')
# # student_5 = Student(studentID='05', firstName='Normal', lastName='Admin', email='admin@demo.com',gender='Male', age='14', IC=910326375515, race='Malay', mobile= '0179097956')

# # session.add(student_1)
# # session.add(student_2)
# # session.add(student_3)
# # session.add(student_4)
# # session.add(student_5)
# # session.commit()

# class Question(Base):
#     __tablename__ = "psy_question"
#     instruCode = Column(String(50), primary_key=True)
#     question = Column(String(50), unique=True, nullable=False)

#     def __repr__(self):
#         return f"Question('{self.question}', '{self.instruCode}')"
# #check table exist
# #if db.engine.dialect.has_table(db.engine, "question"):
# # if db.inspect(db.engine).has_table("student"):
# #     #check row empty
# #     if not Question.query.all():
# # session.add_all([
# #     Question(instruCode='0101', question='TP11 : How are you truely?'),
# #     Question(instruCode='0102', question='TP12 : How fine are you?'),
# #     Question(instruCode='0103', question='TP13 : How good are you?'),
# #     Question(instruCode='0104', question='TP14 : How bulky are you?'),
# #     Question(instruCode='0105', question='TP15 : How anxious are you?'),
# #     Question(instruCode='0106', question='TP16 : How cool are you?'),
# #     Question(instruCode='0107', question='TP17 : How tall are you?'),
# #     Question(instruCode='0108', question='TP18 : How cool are you?'),
# #     Question(instruCode='0109', question='TP19 : How cool are you?'),
# #     Question(instruCode='0110', question='TP20 : How cool are you?'),
    
# #     Question(instruCode='0201', question='TP21 : How much you love?'),
# #     Question(instruCode='0202', question='TP22 : How dare are you?'),
# #     Question(instruCode='0203', question='TP23 : How famous are you?'),
# #     Question(instruCode='0204', question='TP24 : How smelly are you?'),
# #     Question(instruCode='0205', question='TP25 : How low are you?'),
# #     Question(instruCode='0206', question='TP26 : How high are you?'),
# #     Question(instruCode='0207', question='TP27 : How smelly are you?'),
# #     Question(instruCode='0208', question='TP28 : How smelly are you?'),
# #     Question(instruCode='0209', question='TP29 : How smelly are you?'),
# #     Question(instruCode='0210', question='TP30 : How smelly are you?'),

# #     Question(instruCode='0301', question='TP31 : How happy are you?'),
# #     Question(instruCode='0302', question='TP32 : How satisfied are you?'),
# #     Question(instruCode='0303', question='TP33 : How sad are you?'),
# #     Question(instruCode='0304', question='Tp34 : How stupid are you?'),
# #     Question(instruCode='0305', question='Tp35 : How excited are you?'),
# #     Question(instruCode='0306', question='Tp36 : How excited are you?'),
# #     Question(instruCode='0307', question='Tp37 : How excited are you?'),
# #     Question(instruCode='0308', question='Tp38 : How excited are you?'),
# #     Question(instruCode='0309', question='Tp39 : How excited are you?'),
# #     Question(instruCode='0310', question='Tp40 : How excited are you?')
# # ])
# # session.commit()
# # session.add_all([
# #     question_1 = Question(instruCode='0101', question='TP1: How are you?')
# #     question_2 = Question(instruCode='0102', question='TP1 : How fine are you?')
# #     question_3 = Question(instruCode='0103', question='TP2 : How good are you?')
# #     question_4 = Question(instruCode='0104', question='TP1 : How bulky are you?')
# #     question_5 = Question(instruCode='0105', question='TP1 : How anxious are you?')
# #     question_6 = Question(instruCode='0106', question='TP1 : How cool are you?')
# #     question_7 = Question(instruCode='0107', question='TP1 : How tall are you?')
# #     question_8 = Question(instruCode='0108', question='TP1 : How cool are you?')
# #     question_9 = Question(instruCode='0109', question='TP1 : How cool are you?')
# #     question_10 = Question(instruCode='0110', question='TP1 : How cool are you?')
    
# #     question_11 = Question(instruCode='0201', question='TP2 : How much you love?')
# #     question_12 = Question(instruCode='0202', question='TP2 : How dare are you?')
# #     question_13 = Question(instruCode='0203', question='TP2 : How famous are you?')
# #     question_14 = Question(instruCode='0204', question='TP2 : How smelly are you?')
# #     question_15 = Question(instruCode='0205', question='TP2 : How smelly are you?')
# #     question_16 = Question(instruCode='0206', question='TP2 : How smelly are you?')
# #     question_17 = Question(instruCode='0207', question='TP2 : How smelly are you?')
# #     question_18 = Question(instruCode='0208', question='TP2 : How smelly are you?')
# #     question_19 = Question(instruCode='0209', question='TP2 : How smelly are you?')
# #     question_20 = Question(instruCode='0210', question='TP2 : How smelly are you?')

# #     question_21 = Question(instruCode='0301', question='TP3 : How happy are you?')
# #     question_22 = Question(instruCode='0302', question='TP3 : How satisfied are you?')
# #     question_23 = Question(instruCode='0303', question='TP3 : How sad are you?')
# #     question_24 = Question(instruCode='0304', question='Tp3 : How excited are you?')
# #     question_25 = Question(instruCode='0305', question='Tp3 : How excited are you?')
# #     question_26 = Question(instruCode='0306', question='Tp3 : How excited are you?')
# #     question_27 = Question(instruCode='0307', question='Tp3 : How excited are you?')
# #     question_28 = Question(instruCode='0308', question='Tp3 : How excited are you?')
# #     question_29 = Question(instruCode='0309', question='Tp3 : How excited are you?')
# #     question_30 = Question(instruCode='0310', question='Tp3 : How excited are you?')
# # ])
# # for i in range(1,31):
# #     question = "question"+ str(i)
# #     session.add(question) 

# class Elearning(Base):
#     __tablename__ = "psy_elearning"
#     id = Column(String(50),primary_key=True, nullable=False)
#     #kemahiran belajar
#     kb =Column(Float, nullable=True)
#     #kemahiran literasi
#     kl =Column(Float, nullable=True)
#     #kemahiran hidup
#     kh =Column(Float, nullable=True)
#     userID = Column(String(50), nullable=True)

# class Learner(Base):
#     __tablename__ = "psy_learner"
#     id = Column(String(50), primary_key=True, nullable=False)
#     tr1 =Column(Float, nullable=True)
#     userID = Column(String(50), nullable=True)

# class Attitude(Base):
#     __tablename__ = "psy_attitude"
#     id = Column(String(50),primary_key=True, nullable=False)
#     #motivasi
#     mt =Column(Float, nullable=True)
#     #keterbukaan
#     kt =Column(Float, nullable=True)
#     #kestabilan emosi
#     ke =Column(Float, nullable=True)
    
#     userID = Column(String(50), nullable=True)

# class Code(Base):
#     __tablename__ = "psy_code"
#     code = Column(String(50), nullable=False, primary_key=True)
#     desc = Column(String(50), nullable=False)

# # db.create_all()