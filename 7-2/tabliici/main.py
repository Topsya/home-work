
from sqlalchemy import func, desc, select, and_

from models import Teacher, Student, Discipline, Grade, Group, session


def select_1():
     
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    
  
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result

def select_2():
#     Знайти студента із найвищим середнім балом з певного предмета.
    discipline_id = int(input ( 'enter N subject 1-3: '))
    result = session.query(Student.fullname, Discipline.name , func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Discipline).filter(Discipline.id == discipline_id ).group_by(Student.id, Discipline.name).order_by(desc('avg_grade')).limit(1).all()
    return result

def select_3():
# Знайти середній бал у групах з певного предмета.
     discipline_id = int(input ( 'enter N subject 1-5: '))
     result = session.query(Group.name, Discipline.name ,  func.round(func.avg(Grade.grade), 2).label('avg_grade') ) \
        .select_from(Grade).join(Group).join(Discipline).filter(Discipline.id == discipline_id ).group_by( Discipline.name).order_by(desc('avg_grade')).all()
     return result

def select_4():
# # Знайти середній бал на потоці (по всій таблиці оцінок).
  result = session.query( func.round(func.avg(Grade.grade) ))\
        .select_from(Grade).order_by(desc('avg_grade')).limit(1).all()
  return result

def select_5():
# # Знайти, які курси читає певний викладач.
    Teacher_id = int(input ( 'enter id teacher   1-5: '))
    result = session.query(Teacher.fullname, Discipline.name  ) \
        .select_from(Discipline).join(Teacher).join(Discipline).filter(Teacher.id == Teacher_id ).all()
    return result


def select_6():
# # Знайти список студентів у певній групі.
    Group_id = int(input ( 'enter id group  1-3: '))
    result = session.query(Group.name, Student.fullname  ) \
        .select_from(Student).join(Group).filter(Group.id == Group_id ).all()
    return result

def select_7():
# # Знайти оцінки студентів в окремій групі з певного предмета.
    discipline_id = int(input ( 'enter N subject 1-5: '))
    Group_id = int(input ( 'enter id group  1-3: '))
    result = session.query(Student.fullname , Group.name , Discipline.name , Grade.grade  ) \
        .select_from(Student).join(Group ).join(Grade ).filter(Discipline.id == discipline_id, Group.id == Group_id ).group_by(Student.fullname, Discipline.name).all() 
    return result

def select_8():
# # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    Teacher_id = int(input ( 'enter id teacher   1-5: '))
    result = session.query(Teacher.fullname , Discipline.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
       .select_from(Grade).join(Teacher).join(Discipline).filter(Teacher.id == Teacher_id ).group_by(Teacher.fullname).order_by(desc('avg_grade')) .all()
    return result

def select_9():
# # Знайти список курсів, які відвідує певний студент.
    Student_id = int(input ( 'enter id student   1-40: '))
    result = session.query(Student.fullname, Discipline.name ) \
      .select_from(Grade).join(Student).join(Discipline).filter(Student.id == Student_id ).group_by(Discipline.name ).order_by(Group.id).all()
    return result

def select_10():
# # Список курсів, які певному студенту читає певний викладач.
    Student_id = int(input ( 'enter id student   1-40: '))
    Teacher_id = int(input ( 'enter id teacher   1-5: '))
    result = session.query(Student.fullname, Teacher.fullname, Group.name ) \
     .select_from(Grade).join(Student).join(Teacher).join(Discipline).filter(Student.id == Student_id, Teacher.id == Teacher_id ).group_by(Teacher.fullname ).order_by(Group.id).all()
    return result

if __name__ == '__main__':
    print (' 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів\n 2.Знайти студента із найвищим середнім балом з певного предмета\n 3.Знайти середній бал у групах з певного предмета\n 4.Знайти середній бал на потоці (по всій таблиці оцінок)\n 5.Знайти, які курси читає певний викладач\n 6.Знайти список студентів у певній групі\n 7.Знайти оцінки студентів в окремій групі з певного предмета\n 8.Знайти середній бал, який ставить певний викладач зі своїх предметів\n 9.Знайти список курсів, які відвідує студент\n 10.Список курсів, які певному студенту читає певний викладач.')
    i = int (input ('enter comand 0-10 : '))
    if i == 1:
        select_1()
    elif i == 2:
        select_2()
    elif i == 3:
        select_3()
    elif i == 4:
        select_4()
    elif i == 5:
        select_5()
    elif i == 6:
        select_6()
    elif i == 7:
        select_7()
    elif i == 8:
        select_8()
    elif i == 9:
        select_9()
    elif i == 10:
        select_10()
    


