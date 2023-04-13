from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    account_number = Column(String(20), unique=True, nullable=False)
    address = Column(String(100), nullable=False)
    mobile_phone = Column(String(20), unique=True)
    landline = Column(String(20), unique=True)
