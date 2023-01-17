from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base


class Restaurent(Base):
    __tablename__ = 'restaurents'
    placeID = Column(String, primary_key=True)
    parking_lot = Column(String)
