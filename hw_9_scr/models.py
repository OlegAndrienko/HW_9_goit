from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"   
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(50), nullable=False)
    born_date = Column(String(50), nullable=False)
    born_location = Column(String(50), nullable=False)
    description = Column(Text(), nullable=False)
    
    
    
class Qoute(Base):
    __tablename__ = "qoutes"
    qoute_id = Column(Integer, primary_key=True, autoincrement=True)
    tags = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    quote = Column(Text(), nullable=False)