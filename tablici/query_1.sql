

-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

-- import sqlite3


-- def execute_query(sql: str) -> list:
--     with sqlite3.connect('todo.db') as con:
--         cur = con.cursor()
--         cur.execute(sql)
--         return cur.fetchall()


-- sql = 
"""
SELECT  AVG( grade ) 
FROM grades
ORDER BY  avg ( grade)
);
"""

-- print(execute_query(sql))