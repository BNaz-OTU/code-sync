# Write your MySQL query statement below

WITH T1 AS (
SELECT E.employee_id 
FROM Employees AS E
LEFT JOIN Salaries AS S
ON E.employee_id = S.employee_id
WHERE (S.salary IS NULL)

UNION 

SELECT S.employee_id
FROM Employees AS E
RIGHT JOIN Salaries AS S
ON E.employee_id = S.employee_id
WHERE (E.name IS NULL)
)

SELECT *
FROM T1
ORDER BY T1.employee_id