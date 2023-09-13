-- # Знайти середній бал, який ставить певний викладач зі своїх предметів.
-- WHERE    subject_id  =  задати номер ід певного предмету от 1 до 8


SELECT  teachers_id , sub.name, AVG(g.grade) 
FROM subjects as sub  
 
JOIN grades as g on g.subject_id = sub.id  
WHERE  sub.id  = 2
 

