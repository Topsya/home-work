
-- Знайти студента із найвищим середнім балом з певного предмета.

SELECT    g.grade ,  st.name , sub.name 
FROM grades as g
JOIN students as st on st.id  = g.student_id  
JOIN subjects as sub on sub.id  = g.subject_id  
limit 8