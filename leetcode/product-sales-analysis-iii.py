# Write your MySQL query statement below
-- Useful comment from the "discussion" board: https://leetcode.com/problems/product-sales-analysis-iii/description/comments/1929476/

WITH T1 AS (
    SELECT 
        *,
        RANK() OVER(PARTITION BY product_id ORDER BY year) AS "ranked"
    FROM Sales
)

SELECT
    product_id,
    year AS "first_year",
    quantity,
    price
FROM T1
WHERE ranked = 1
-- GROUP BY product_id