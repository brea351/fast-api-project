from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    phone = Column(String(15))
    addresses = relationship("Address", back_populates="contact", cascade="all, delete")
    tags = relationship("Tag", back_populates="contact", cascade="all, delete")

class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"))
    street = Column(String(100))
    city = Column(String(50))
    country = Column(String(50))
    contact = relationship("Contact", back_populates="addresses")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"))
    tag_name = Column(String(50))
    contact = relationship("Contact", back_populates="tags")
