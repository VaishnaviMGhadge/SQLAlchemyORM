from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Integer,String,Column

# 1. create engine

engine=create_engine(url="sqlite:///sample.db",echo=True)


# 2. create session
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()

#3. create table

class Student(Base):
    __tablename__='students'
    id=Column(Integer,primary_key=True)
    name=Column(String(20))
    age=Column(Integer)
    grade=Column(String(20))


student1=Student(name='shreya',age=10,grade='fifth')
student2=Student(name='vivek',age=9,grade='fourth')
student3=Student(name='vaivi',age=5,grade='first')

session.add(student1)
session.add(student2)
session.add(student3)

#session.add_all([student1,student2,student3])
session.commit()



#4. Migrate
    #Base.metadata.create_all(engine)


q=session.query(Student).order_by(Student.name)
    
