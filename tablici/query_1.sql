

-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT    student_id  ,  grade , name 
FROM grades as g
JOIN students as st on st.id  = g.student_id 
limit 5 
