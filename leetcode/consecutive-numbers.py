# Write your MySQL query statement below
WITH T1 AS (
SELECT 
    *,
    LAG(num, 1) OVER(ORDER BY id) AS "prev_1_step",
    LAG(num, 2) OVER(ORDER BY id) AS "prev_2_step"
FROM Logs
)

SELECT 
    DISTINCT(num) AS "ConsecutiveNums"
FROM T1
WHERE (num = prev_1_step) AND (num = prev_2_step) AND (prev_1_step = prev_2_step)