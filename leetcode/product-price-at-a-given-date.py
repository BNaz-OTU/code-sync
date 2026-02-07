# Write your MySQL query statement below

WITH T1 AS (
    SELECT 
        product_id,
        MAX(change_date) AS "date"
    FROM Products
    WHERE change_date <= "2019-08-16"
    GROUP BY product_id
    HAVING MAX(change_date)
)

SELECT 
    P.product_id,
    P.new_price AS "price"
FROM Products AS P
JOIN T1
ON P.product_id = T1.product_id AND T1.date = P.change_date

UNION 

SELECT 
    product_id,
    10 AS "price"
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > "2019-08-16"