-- # Знайти список студентів у певній групі.
-- WHERE  g.id  ід групи їх 3

SELECT    g.name  , st.name   
FROM students  as st  
JOIN groups as g on g.name  = st.groups_id  
WHERE  g.id = 2
 
 