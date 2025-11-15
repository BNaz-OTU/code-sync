# Write your MySQL query statement below

SELECT Emp.name AS 'Employee'
FROM Employee AS Emp
JOIN Employee AS Mgr
ON Emp.managerId = Mgr.id
WHERE Emp.salary > Mgr.salary