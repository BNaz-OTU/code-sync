# Write your MySQL query statement below

WITH T1 AS (
    SELECT COUNT(*) AS "total_products"
    FROM Product
)

SELECT 
    customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT total_products FROM T1)