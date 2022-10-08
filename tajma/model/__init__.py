from tajma import login_manager, engine
from tajma.model.UserModel import User
from sqlalchemy.orm import sessionmaker

# db.drop_all()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

@login_manager.user_loader
def load_user(user_id):
    print(f'user is : {session.query(User).get(user_id)}')
    return session.query(User).get(user_id)

def db_insert_data(model):
    session.add(model)
    session.commit()

def db_update_data():
    session.commit()