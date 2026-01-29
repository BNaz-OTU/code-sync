# Write your MySQL query statement below

-- USED SOLN: https://www.youtube.com/watch?v=Vi4-AraAvgk

WITH CTE AS (
    SELECT 
        S.*,
        P.category,
    CASE
        WHEN MONTH(S.sale_date) = 12 OR MONTH(S.sale_date) BETWEEN 1 AND 2 THEN "Winter"
        WHEN MONTH(S.sale_date) BETWEEN 3 AND 5 THEN "Spring"
        WHEN MONTH(S.sale_date) BETWEEN 6 AND 8 THEN "Summer"
        WHEN MONTH(S.sale_date) BETWEEN 9 AND 11 THEN "Fall"
        END AS season
    FROM sales AS S
    LEFT JOIN products AS P
    ON S.product_id = P.product_id
),

CTE2 AS (
    SELECT 
        season,
        category,
        SUM(quantity) AS "total_quantity",
        SUM(quantity * price) AS "total_revenue"
    FROM CTE
    GROUP BY season, category
),

CTE3 AS (SELECT *, ROW_NUMBER() OVER(PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC) AS rnk
FROM CTE2)

SELECT 
    season,
    category,
    total_quantity,
    total_revenue
FROM CTE3
WHERE rnk = 1
ORDER BY season ASC