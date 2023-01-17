from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base


class RestaurentParking(Base):
    __tablename__ = 'restaurant_parking'
    placeID = Column(String, ForeignKey(
        'restaurents.placeID', ondelete='CASCADE'), primary_key=True)
    parking_lot = Column(String, primary_key=True)

    restaurent = relationship("restaurents", backref="restaurant_parking")
