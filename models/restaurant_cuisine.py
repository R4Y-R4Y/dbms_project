from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base


class RestaurentCuisine(Base):
    __tablename__ = 'restaurant_cuisine'
    placeID = Column(String, ForeignKey(
        'restaurents.placeID', ondelete='CASCADE'), primary_key=True)
    Rcuisine = Column(String, primary_key=True)
    restaurent = relationship("restaurents", backref="restaurant_cuisine")
