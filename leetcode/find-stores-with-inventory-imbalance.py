# Write your MySQL query statement below
WITH T1 AS(
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price DESC) AS "expensive",
        ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price) AS "cheap"
    FROM inventory
),

T2 AS (
    SELECT 
        store_id,
        MAX(CASE WHEN expensive = 1 THEN product_name ELSE NULL END) AS "most_exp_product",
        MAX(CASE WHEN cheap = 1 THEN product_name ELSE NULL END) AS "cheapest_product",
        SUM(CASE WHEN expensive = 1 THEN quantity ELSE NULL END) AS "exp_qty",
        SUM(CASE WHEN cheap = 1 THEN quantity ELSE NULL END) AS "chp_qty"
    FROM T1
    GROUP BY store_id
    HAVING COUNT(*) >= 3
)

SELECT 
    S.*,
    T2.most_exp_product,
    cheapest_product,
    ROUND(chp_qty / exp_qty, 2) AS "imbalance_ratio"
FROM T2
JOIN stores AS S
ON T2.store_id = S.store_id
WHERE exp_qty < chp_qty
ORDER BY imbalance_ratio DESC, store_name