from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base


class RestaurentHours(Base):
    __tablename__ = 'restaurant_hours'
    placeID = Column(String, ForeignKey(
        'restaurents.placeID', ondelete='CASCADE'), primary_key=True)
    hours = Column(String, primary_key=True)
    days = Column(String, primary_key=True)
    restaurent = relationship("restaurents", backref="restaurant_hours")
