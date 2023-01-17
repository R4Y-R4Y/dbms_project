from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, dialects
from sqlalchemy.orm import relationship
from database import Base


class UserPayment(Base):
    __tablename__ = 'user_payment'
    userID = Column(String, ForeignKey(
        'users.userID', ondelete='CASCADE'), primary_key=True)
    Upayment = Column(String, primary_key=True)
    user = relationship("users", backref="user_payment")
