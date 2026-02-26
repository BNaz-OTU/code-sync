# Write your MySQL query statement below
WITH T1 AS (
    SELECT 
        *,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS "RANKED" 
    FROM Employee
)

SELECT 
    MAX(salary) AS "SecondHighestSalary"
FROM T1
WHERE RANKED = 2