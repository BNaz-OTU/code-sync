# Write your MySQL query statement below

SELECT 
    MGR.employee_id,
    MGR.name,
    COUNT(*) AS "reports_count",
    ROUND(AVG(E1.age), 0) AS "average_age"
FROM Employees AS E1
JOIN Employees AS MGR
ON E1.reports_to = MGR.employee_id
GROUP BY MGR.employee_id
ORDER BY MGR.employee_id