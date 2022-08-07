from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Department, Employee, Role

engine = create_engine('sqlite:///database.sqlite3')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
s = db_session()
#from database import *

Employee.__table__.create(engine)
Role.__table__.create(engine)
Department.__table__.create(engine)
e=Department(name='Engineering')
s.add(e)
h=Department(name='HR')
s.add(h)
m=Role(name='manager')
s.add(m)
ee=Role(name='engineer')
s.add(ee)
p=Employee(name='Peter Pan', department=e, role=ee)
s.add(p)
t=Employee(name='Tracy Chapman',department=h,role=m)
s.add(t)
s.commit()
