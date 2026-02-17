# Write your MySQL query statement below

WITH T1 AS (
    SELECT 
        managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)

SELECT
    E.name
FROM Employee AS E
JOIN T1
ON E.id = T1.managerId