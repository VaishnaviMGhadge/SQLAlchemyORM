from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import  Integer,String,Column
from sqlalchemy import create_engine

# 1. create engine
engine=create_engine(url='sqlite:///sample.db',echo=True)

# 2. create session
Session=sessionmaker(bind=engine)
session=Session()

Base=declarative_base()


# 3. create table
class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True)
    name=Column(String(10))
    age=Column(Integer)
    grade=Column(String(3))



# 4. Migrate
    
Base.metadata.create_all(engine)

# 1. create engine
# 2. create session
# 3. create table
# 4. Migrate