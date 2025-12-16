# Write your MySQL query statement below

WITH T1 AS (SELECT *
FROM MyNumbers
GROUP BY num
HAVING COUNT(*) = 1)

SELECT MAX(T1.num) AS "num"
FROM T1