from  insertintotable import *

S1=session.query(Student).filter(Student.name=='shreya').first()
session.delete(S1)
session.commit()