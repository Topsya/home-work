-- # Список курсів, які певному студенту читає певний викладач.
-- WHERE  s.id  = ід студіка від 1 до 40  AND t.id = ід вчителя 1-5


SELECT s.name , t.name , sub.name 
FROM grades   as g   
JOIN subjects as sub on sub.id  = g.subject_id  
JOIN students  as s  on s.id  = g.student_id  
JOIN teachers as t on t.id = sub.id 
WHERE  s.id  = 3 AND t.id = 2
