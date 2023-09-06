import sqlite3
from faker import Faker
from random import randint
import random 
from datetime import datetime

def create_db():
    with open('init_todo.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect("todo.db") as con:
        cur = con.cursor()
        cur.executescript(sql)

        

def populate_db():
    students_sql_command = "\n".join(f"INSERT INTO students (name) VALUES ('{Faker().name()}');" for _ in range(40))
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(students_sql_command)
        cur.execute("SELECT name from students;")
        # students_ids = [obj[0] for obj in cur.fetchall()] 
        students_name = [obj[0] for obj in cur.fetchall()] 
        # print(students_name)       
       


    groups_sql_command = "\n".join(f"INSERT INTO groups (name) VALUES ('groups N{i}');"  for i in range(3))
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(groups_sql_command)
        cur.execute("SELECT name from groups;")
        groups_name = [obj[0] for obj in cur.fetchall()]        
        # print(groups_name)
    
    teachers_sql_command = "\n".join(f"INSERT INTO teachers (name) VALUES ('{Faker().name()}');" for _ in range(7))
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(teachers_sql_command)
        cur.execute("SELECT name from teachers;")
        teachers_name = [obj[0] for obj in cur.fetchall()]        
        # print(teachers_name)
    
    subjects_sql_command = "\n".join(f"INSERT INTO subjects (name, subjects_teachers) VALUES ('subjects N {j+1}', '{teachers_name[j] }' );" for j in range(5) )
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(subjects_sql_command)
        cur.execute("SELECT * from subjects;") 
        subjects_name =  [ obj[1] for obj in cur.fetchall()]
        # print(subjects_name)

    
   
   
    
    grade_sql_command = """ CREATE TABLE grades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    student_id INT,
                    subject_id INT,
                     
                    date_of TIMESTAMP DEFAULT CURRENT_TIMESTAMP  NOT NULL,
                    grade NOT NULL,

                    FOREIGN KEY (student_id) REFERENCES  students (id)
                    FOREIGN KEY (subject_id) REFERENCES  subjects (id)
                      ON DELETE SET NULL

                );"""
    # with sqlite3.connect('todo.db') as con:
    #         cur = con.cursor()
    #         cur.execute(grade_sql_command)
    #         cur.close()

    for_grades = []
    
    for student_id in range(1, len(students_name) + 1):
        for subject_id in range(1, len(subjects_name) + 1):
            for _ in range(randint(1, 20)):
                    date_of = datetime.now()
                    grade = randint(1, 12)
                    for_grades.append((student_id, subject_id, date_of, grade))


    grade_sql_command = """INSERT INTO  grades (student_id, subject_id, date_of, grade)
                                VALUES (?, ?, ?, ?)"""
    cur.executemany(grade_sql_command, for_grades)

    con.commit()
 
def check_db():
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from students;")
        result = cur.fetchall()
    print(result)

    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from groups;")
        result = cur.fetchall()
    print(result)

    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from teachers;")
        result = cur.fetchall()
    print(result)

    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from subjects;")
        result = cur.fetchall()
    print(result)

    # with sqlite3.connect('todo.db') as con:
    #     cur = con.cursor()
    #     cur.execute("SELECT * from grades;")
    #     result = cur.fetchall()
    # print(result)


def select(table_name:str, condition=None):
    if condition is not None:
        querry = f"SELECT * FROM {table_name} WHERE {condition};"
    else:
        querry = f"SELECT * FROM {table_name};"


    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(querry)
        result = cur.fetchall()
    return result

def delete(table_name:str, condition=None):
    if condition is not None:
        querry = f"DELETE  FROM {table_name} WHERE {condition};"
    else:
        querry = f"DELETE  FROM {table_name};"


    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(querry)
        result = cur.fetchall()
    return result



create_db()
populate_db()
check_db()


