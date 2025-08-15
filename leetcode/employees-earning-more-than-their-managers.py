# Write your MySQL query statement below

SELECT EMP.name AS 'Employee'
FROM Employee AS EMP
LEFT JOIN Employee AS MGR
ON EMP.managerId = MGR.id
WHERE EMP.salary > MGR.salary