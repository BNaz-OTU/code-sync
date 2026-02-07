# Write your MySQL query statement below

-- Get the products that changed price before 2019-08-16 and find the closest date to 2019-08-16

-- USED FOR REF: https://www.youtube.com/watch?v=a7xb-Q6WoW8

WITH T1 AS (
    SELECT 
        product_id,
        MAX(change_date) AS "date"
    FROM Products
    WHERE change_date <= "2019-08-16"
    GROUP BY product_id
)

-- From T1, use its data to join with the exisiting table to locate the most recent price change before or
-- on the day of the price change date (2019-08-16)
SELECT 
    P.product_id,
    P.new_price AS "price"
FROM Products AS P
JOIN T1
ON P.product_id = T1.product_id AND T1.date = P.change_date

UNION 

-- When a product didn't change price until after 2019-08-16
SELECT 
    product_id,
    10 AS "price"
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > "2019-08-16"