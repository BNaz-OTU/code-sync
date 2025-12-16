# Write your MySQL query statement below

-- SOLN: https://leetcode.com/problems/biggest-single-number/solutions/7334691/very-easy-solution-with-logic-explainati-wlco

WITH T1 AS (SELECT *
FROM MyNumbers
GROUP BY num
HAVING COUNT(*) = 1)

SELECT MAX(T1.num) AS "num"
FROM T1