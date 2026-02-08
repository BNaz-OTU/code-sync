# Write your MySQL query statement below

-- Find the Max Salary in each department
WITH T1 AS (
    SELECT 
        departmentId,
        MAX(salary) AS "max_sal"
    FROM Employee
    GROUP BY departmentId
),


-- Find the employees with those max salaries
T2 AS (
    SELECT 
        E.name, 
        E.departmentId,
        E.salary
    FROM Employee AS E
    JOIN T1
    ON (T1.max_sal = E.salary) AND (T1.departmentId = E.departmentId)
)


-- Include the Department name with the employee info (Final answer)
SELECT
    D.name AS "Department",
    T2.name AS "Employee",
    T2.salary AS "Salary"
FROM T2
JOIN Department AS D
ON T2.departmentId = D.id