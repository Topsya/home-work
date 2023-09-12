

-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT  st.name , sub.name , avg(grade )
FROM grades as g
JOIN students as st on st.id  = g.student_id  
JOIN subjects as sub on sub.id  = g.subject_id  
--WHERE  
ORDER BY avg(grade) 
limit 5
