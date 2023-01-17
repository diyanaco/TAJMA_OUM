from sqlalchemy import event
from models import engine

def my_on_checkout(dbapi_conn, connection_rec, connection_proxy):
    "handle an on checkout event"

event.listen(engine, 'checkout', my_on_checkout)