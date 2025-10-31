from sqlalchemy import (Column, Integer, String, ForeignKey, Numeric,
                        CheckConstraint, Text)
from sqlalchemy.orm import relationship
from .database import Base, engine


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String(20), nullable=False)
    gmail = Column(String(100), nullable=False)
    subject = Column(String(255))
    message = Column(Text)


Base.metadata.create_all(bind=engine)
