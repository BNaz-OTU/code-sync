# Write your MySQL query statement below

WITH T1 AS (
    SELECT COUNT(*) AS "total_users"
    FROM Users
)

SELECT 
    contest_id, 
    ROUND((COUNT(user_id) / total_users) * 100, 2) AS "percentage"
FROM Register
CROSS JOIN T1
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC