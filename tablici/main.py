
from repository import *

from modeli import *
# import query_1.sql


def check_db():
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(""" SELECT   grade      
                    FROM grades LIMIT 5
                    JOIN students and subjects
                    ORDER BY AVG(grade)                     
                     
                     ;""")
        result = cur.fetchall()
        print(result)
        cur.close()

check_db()


