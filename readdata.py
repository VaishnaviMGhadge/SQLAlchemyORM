from sqlalchemy import create_engine
from sqlalchemy import Integer,Column,String
from sqlalchemy.orm import declarative_base,sessionmaker

engine=create_engine(url='sqlite:///sample.db',echo=True)

Session=sessionmaker(bind=engine)
session=Session()

Base=declarative_base()

class Book(Base):
    __tablename__='books'
    book_id=Column(Integer,primary_key=True)
    name=Column(String(30))
    author=Column(String(20))
    price=Column(Integer)

#Base.metadata.create_all(engine)

b1=Book(name='atomic habits',author='james clear',price=2000)
b2=Book(name='Let us C',author='Yashwant kanetkar',price=609)
b3=Book(name="python programming",author='blackbook',price=789)

#session.add_all([b1,b2,b3])
#session.commit()


books=session.query(Book).filter(Book.name=='python programming').first()

if books:
    books.name = 'Java Programming'
    session.commit()

#session.commit
#print(books)
"""for book in books:
    print(book.name)"""


##get data in order by students name 

