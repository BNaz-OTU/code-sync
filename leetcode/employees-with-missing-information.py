# Write your MySQL query statement below

WITH T1 AS (SELECT employee_id, name
FROM Employees

UNION 

SELECT employee_id, salary
FROM Salaries)

SELECT employee_id
FROM T1
GROUP BY employee_id
HAVING COUNT(*) = 1
ORDER BY employee_id ASC