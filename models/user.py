from sqlalchemy import Date, Boolean, Column, ForeignKey, Integer, String, DateTime, Enum, Float, dialects
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    userID = Column(String, primary_key=True)
    drink_level = Column(String)
    dress_preference = Column(String)
    ambience = Column(String)
    transport = Column(String)
    marital_status = Column(String)
    hijos = Column(String)
    birth_year = Column(Integer)
    interest = Column(String)
    personality = Column(String)
    religion = Column(String)
    activity = Column(String)
    color = Column(String)
    budget = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    weight = Column(Float)
    height = Column(Float)
