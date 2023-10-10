# Ім'я
# Прізвище
# Електронна адреса
# Номер телефону
# День народження

from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import date
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql.schema import ForeignKey
# from  pydantic import BaseModel, EmailStr
# from  sqlalchemy_utils import EmailType, PhoneNumber
# from sqlalchemy.dialects import plugins
# from sqlalchemy import dialects

Base = declarative_base()
 
class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    surname =  Column(String , index=True)
    email = Column(String, unique=True, index=True)
    fonenamber = Column(String ,index=True)
    birthday = Column(Date )

 