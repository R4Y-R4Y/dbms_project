from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base


class UserCuisine(Base):
    __tablename__ = 'user_cuisine'
    userID = Column(String, ForeignKey(
        'users.userID', ondelete='CASCADE'), primary_key=True)
    Rcuisine = Column(String, primary_key=True)
    user = relationship("users", backref="user_cuisine")
