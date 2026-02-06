# Write your MySQL query statement below

-- USED SOLN: https://www.youtube.com/watch?v=M29s5Zdt2iU

WITH T1 AS (SELECT 
    U.user_id,
    SUM(IF(YEAR(O.order_date) = 2019, 1, 0)) AS "orders_in_2019"
FROM Users AS U
LEFT JOIN Orders AS O
ON O.buyer_id = U.user_id
GROUP BY U.user_id)

SELECT
    C.user_id AS "buyer_id", 
    U.join_date,
    C.orders_in_2019
FROM T1 AS C
LEFT JOIN Users AS U
ON C.user_id = U.user_id