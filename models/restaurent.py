from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base


class Restaurent(Base):
    __tablename__ = 'restaurents'
    placeID = Column(Integer, primary_key=True)
    Rpayment = Column(dialects.postgresql.ARRAY(String))
    Rcuisine = Column(dialects.postgresql.ARRAY(String))
    hours = Column(dialects.postgresql.ARRAY(String))
    days = Column(dialects.postgresql.ARRAY(String))
    parking_lot = Column(String)
