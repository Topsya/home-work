from datetime import datetime

class Stusent:
    def __init__(self, name=str ):
          self.name = name

class Groups:
    def __init__(self, groups= str ):
          self.groups = groups

class   Teachers :
     def __init__(self, teachers= str ):
          self.teachers = teachers    

class Subjects :
     def __init__(self, subjects= str ):
          self.subjects = subjects    

class Grade :
     def __init__(self, grade= int, wen_time= datetime ):
          self.grade = grade   
          self.wen_time =  wen_time

