# Write your MySQL query statement below

-- USED SOLN: https://www.youtube.com/watch?v=Td452uOq-80

SELECT 
    Q1.person_name
FROM Queue AS Q1 
JOIN Queue AS Q2
ON Q1.turn >= Q2.turn
GROUP BY Q1.turn
HAVING SUM(Q2.weight) <= 1000
ORDER BY Q1.turn DESC
LIMIT 1