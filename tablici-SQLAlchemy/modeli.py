from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///student.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()




class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(120), nullable=False)
    group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))
    group = relationship('Groups', backref='students')

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

class   Teachers(Base):
     __tablename__ = 'teachers'
     id = Column(Integer, primary_key=True)
     fullname = Column(String(120), nullable=False)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship('Teacher', backref='disciplines')

class Grade(Base):
     __tablename__ = 'grades'
     id = Column(Integer, primary_key=True)      
     grade = Column(Integer, nullable=False)
     date_of = datetime.now() 
     student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
     discipline_id = Column('Subject_id', ForeignKey('subjects.id', ondelete='CASCADE'))
     student = relationship('Student', backref='grade')
     discipline = relationship('Subject', backref='grade')

