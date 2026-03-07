# Write your MySQL query statement below
WITH T1 AS (
    SELECT 
        product_id,
        MIN(S.year) AS "first_year"
    FROM Sales AS S
    GROUP BY product_id
)

SELECT 
    S2.product_id,
    T1.first_year,
    S2.quantity,
    S2.price
FROM T1
JOIN Sales AS S2
ON T1.product_id = S2.product_id AND T1.first_year = S2.year