# Write your MySQL query statement below
-- USED SOLN: https://www.youtube.com/watch?v=m4nFxP_2iRU

WITH T1 AS (
    SELECT *,
        ROW_NUMBER() OVER(PARTITION BY store_id ORDER BY price DESC) AS "exp_rnk",
        ROW_NUMBER() OVER(PARTITION BY store_id ORDER BY price) AS "chp_rnk"
    FROM inventory
),

T2 AS (
    SELECT 
        store_id,
        MAX(CASE WHEN exp_rnk = 1 THEN product_name ELSE NULL END) AS "most_exp_product",
        MIN(CASE WHEN chp_rnk = 1 THEN product_name ELSE NULL END) AS "cheapest_product",
        SUM(CASE WHEN exp_rnk = 1 THEN quantity ELSE 0 END) AS "exp_qty",
        SUM(CASE WHEN chp_rnk = 1 THEN quantity ELSE 0 END) AS "chp_qty"
    FROM T1
    GROUP BY store_id
    HAVING COUNT(DISTINCT product_name) >= 3
)

SELECT 
    S.*,
    T2.most_exp_product,
    T2.cheapest_product,
    ROUND((T2.chp_qty / T2.exp_qty), 2) AS "imbalance_ratio"
FROM T2
JOIN stores AS S
ON T2.store_id = S.store_id
WHERE T2.exp_qty < chp_qty
ORDER BY imbalance_ratio DESC, S.store_name ASC