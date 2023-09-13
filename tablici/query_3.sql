-- # Знайти середній бал у групах з певного предмета.
-- WHERE    subject_id  =  задати номер ід певного предмету от 1 до 8

SELECT g2.name , sub.name , AVG(grade)
FROM grades as g
JOIN groups  as g2 on g2.id  = g.subject_id  
JOIN subjects as sub on sub.id  = g.subject_id  
WHERE    subject_id  = 1
ORDER BY avg(grade) 

