# from datetime import datetime

class Student:
    def __init__(self, name=str ):
          self.name = name

class Groups:
    def __init__(self, groups= str ):
          self.groups = groups

class   Teachers :
     def __init__(self, teachers= str ):
          self.teachers = teachers    

class Subjects :
     def __init__(self, subjects= str, subjects_teachers= str):
          self.subjects = subjects   
          self.subjects_teachers = subjects_teachers 

class Grade :
     def __init__(self,grades_by_subject, student= str, subjects= str):
          
          self.grades_by_subject = grades_by_subject 
          self.student = student 
          self.subjects = subjects   
          

