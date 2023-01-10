from sqlalchemy import Date, Boolean, Column, ForeignKey, Integer, String, DateTime, Enum, Float, dialects
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    userID = Column(Integer, primary_key=True)
    smoker = Column(Boolean)
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
    Rcuisine = Column(dialects.postgresql.ARRAY(String))
    Upayment = Column(dialects.postgresql.ARRAY(String))
    latitude = Column(Float)
    longitude = Column(Float)
    weight = Column(FLoat)
    height = Column(Float)
