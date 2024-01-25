from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine

engine=create_engine(url="sqlite:///sample.db",echo=True)


class Base(DeclarativeBase):
    pass
