-- # Знайти список курсів, які відвідує студент.
-- WHERE  s.id  = ід студента 1 до 40 

SELECT s.name , sub.name 
FROM grades   as g   
JOIN subjects as sub on sub.id  = g.subject_id  
JOIN students  as s  on s.id  = g.student_id  
WHERE  s.id  = 3
 