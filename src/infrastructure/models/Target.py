from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Target(Base):
    __tablename__ = 'targets'
    id = Column(String, primary_key=True)
    x = Column(Float)
    y = Column(Float)
