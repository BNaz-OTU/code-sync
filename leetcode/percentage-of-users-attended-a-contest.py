# Write your MySQL query statement below

WITH T1 AS (
    SELECT COUNT(*) AS 'p'
    FROM Users
)

SELECT 
    R.contest_id, 
    ROUND((COUNT(R.contest_id) / T1.p) * 100, 2) AS 'percentage'
FROM Register AS R, T1
GROUP BY R.contest_id
ORDER BY percentage DESC, contest_id ASC