# Write your MySQL query statement below

-- USED SOLN: https://www.youtube.com/watch?v=9G_yYnKcOFo

WITH T1 AS
(
    SELECT *,
        CASE
            WHEN order_date = customer_pref_delivery_date THEN "immediate"
            ELSE "scheduled"
        END AS "Pref"
    FROM Delivery
),


T2 AS (
    SELECT 
        customer_id,
        MIN(order_date) AS "first_date"
    FROM Delivery
    GROUP BY customer_id
)

SELECT 
    ROUND((SUM(T1.Pref = "immediate") / COUNT(T1.Pref)) * 100, 2) AS "immediate_percentage"
FROM T1
JOIN T2
ON T1.order_date = T2.first_date AND T1.customer_id = T2.customer_id


-- Be careful with this part:
-- ON T1.order_date = T2.first_date AND T1.customer_id = T2.customer_id

-- I first only had --- ON T1.order_date = T2.first_date --- but this could lead to errors, since
-- I'm only checking to make sure the dates are the same, there could be orders where multiple customers have
-- the same order date, this join could cause duplications because it only compares the dates and doesn't check the 
-- customer_id. This line fixes it: --- ON T1.order_date = T2.first_date AND T1.customer_id = T2.customer_id ----