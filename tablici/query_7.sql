-- # Знайти оцінки студентів в окремій групі з певного предмета.
-- WHERE  g.id =  ід групи до 3

SELECT   g.name  , st.name, g2.grade  
FROM students  as st  
JOIN groups as g on g.name  = st.groups_id  
JOIN grades as g2 on g2.student_id  = st.id 
WHERE  g.id = 2
 
 

