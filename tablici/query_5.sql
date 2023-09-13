-- # Знайти, які курси читає певний викладач.
-- WHERE  t.id =  ід певного викладача їх від 1 до 5

SELECT   t.name , sub.name  
FROM subjects as sub  
JOIN teachers as t on t.name  = sub.teachers_id 
WHERE  t.id = 3
 
 