from tajma import db

class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=True )
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    profPic = db.Column(db.String(20), nullable=False, default = 'default.jpg')
    
    def __repr__(self):
       return f"User('{self.email}', '{self.password}')"

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