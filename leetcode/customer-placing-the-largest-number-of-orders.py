# Write your MySQL query statement below

SELECT customer_number
FROM Orders 
GROUP BY customer_number
-- HAVING COUNT(*) 
ORDER BY COUNT(*) DESC
LIMIT 1