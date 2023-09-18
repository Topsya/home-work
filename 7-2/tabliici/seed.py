
from faker import Faker
from datetime import date, datetime, timedelta
from sqlalchemy import select
from models import Teacher, Student, Discipline, Grade, Group, session
from random import randint, choice

group =  Group(name="Group")

fake = Faker()



groups = ["grup N1", "grup N2", "grup N3"]

 
number_of_teachers = 5
number_of_students = 40
disciplines = [
        "Subgect 1",
        "Subgect 2",
        "Subgect 3",
        "Subgect 4",
        "Subgect 5"
    ]

def date_range(start: date, end: date) -> list:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result

def seed_teachers():
        for _ in range(number_of_teachers):
            teacher = Teacher(fullname=fake.name())
            session.add(teacher)
        session.commit()

def seed_disciplines():
    teacher_ids = session.scalars(select(Teacher.id)).all()
    for discipline in range(6):
        session.add(Discipline(name=f'name of subject {discipline}', teacher_id=choice(teacher_ids)))
    session.commit()

def seed_groups():
    for group in groups:
        session.add(Group(name=group))
    session.commit()

def seed_students():
    group_ids = session.scalars(select(Group.id)).all()
    for _ in range(number_of_students):
        student = Student(fullname=fake.name(), group_id=choice(group_ids))
        session.add(student)
    session.commit()

def seed_grades():
    # дата початку навчального процесу
    start_date = datetime.strptime("2020-09-01", "%Y-%m-%d")
    # дата закінчення навчального процесу
    end_date = datetime.strptime("2021-05-25", "%Y-%m-%d")
    d_range = date_range(start=start_date, end=end_date)
    discipline_ids = session.scalars(select(Discipline.id)).all()
    student_ids = session.scalars(select(Student.id)).all()

    for d in d_range:  # пройдемося по кожній даті
        random_id_discipline = choice(discipline_ids)
        random_ids_student = [choice(student_ids) for _ in range(5)]
        # проходимося списком "везучих" студентів, додаємо їх до результуючого списку
        # і генеруємо оцінку
        for student_id in random_ids_student:
            grade = Grade(
                grade=randint(1, 12),
                date_of=d,
                student_id=student_id,
                discipline_id=random_id_discipline,
            )
            session.add(grade)
    session.commit()


if __name__ == "__main__":

    seed_teachers()
    seed_disciplines()
    seed_groups()
    seed_students()
    seed_grades()