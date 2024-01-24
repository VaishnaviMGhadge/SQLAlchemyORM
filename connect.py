from sqlalchemy import create_engine,text

engine=create_engine(url='sqlite:///sample.db',echo=True)


with engine.connect() as conn:
    res=conn.execute(text("select 'hello'"))
    print(res.all())