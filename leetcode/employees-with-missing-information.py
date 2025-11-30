# Write your MySQL query statement below

WITH T1 AS (SELECT E.employee_id, E.name, S.salary
FROM Employees AS E
LEFT JOIN Salaries AS S
ON E.employee_id = S.employee_id

UNION

SELECT S.employee_id, E.name, S.salary
FROM Employees AS E
RIGHT JOIN Salaries AS S
ON E.employee_id = S.employee_id)

SELECT T1.employee_id
FROM T1
WHERE (T1.name IS NULL) OR (T1.salary IS NULL)
ORDER BY T1.employee_id ASC