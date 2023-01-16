from sqlalchemy import Date, Boolean, Column, ForeignKey, Integer, String, DateTime, Enum, Float, dialects
from sqlalchemy.orm import relationship
from database import Base


class Rating(Base):
    __tablename__ = 'ratings'
    userID = Column(String, ForeignKey(
        'users.userID', ondelete='CASCADE'), primary_key=True)
    placeID = Column(String, ForeignKey(
        'restaurents.placeID', ondelete='CASCADE'), primary_key=True)
    rating = Column(Integer)
    food_rating = Column(Integer)
    service_rating = Column(Integer)
    user = relationship("User", backref="ratings")
    restaurent = relationship("Restaurent", backref="ratings")
