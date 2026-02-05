# Write your MySQL query statement below

-- USED SOLN: https://www.youtube.com/watch?v=6p9lY_YftsE

SELECT DISTINCT visited_on,
SUM(amount) OVER (ORDER BY visited_on ASC RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS "amount",
ROUND((SUM(amount) OVER (ORDER BY visited_on ASC RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW)/7), 2) AS "average_amount"
FROM Customer
LIMIT 1000000000000 OFFSET 6