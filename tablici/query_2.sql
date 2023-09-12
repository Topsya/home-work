
-- Знайти студента із найвищим середнім балом з певного предмета.

SELECT  st.name , sub.name ,AVG(grade)
FROM grades as g
JOIN students as st on st.id  = g.student_id  
JOIN subjects as sub on sub.id  = g.subject_id  
WHERE  subject_id = 2
ORDER BY avg(grade)