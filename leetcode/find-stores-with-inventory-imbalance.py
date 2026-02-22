-- Write your PostgreSQL query statement below
-- USED SOLN: https://leetcode.com/problems/find-stores-with-inventory-imbalance/solutions/7004525/simple-solution-ez-to-understand-join-ro-uwih

WITH T1 AS (
    SELECT 
        I.store_id,
        I.product_name,
        I.quantity,
        MAX(I.price) AS "Max_Price",
        MIN(I.price) AS "Min_Price"
    FROM inventory AS I
    GROUP BY I.store_id
    HAVING COUNT(DISTINCT product_name) >= 3
),

T2 AS (
    SELECT 
        I.store_id,
        I.product_name,
        I.quantity,
        I.price
    FROM T1
    JOIN inventory AS I 
    ON T1.store_id = I.store_id AND (I.price = T1.Max_Price OR I.price = T1.Min_Price)
),

T3 AS (
    SELECT 
        Max_T.store_id,
        Max_T.product_name AS "most_exp_product",
        Max_T.quantity AS "exp_qty",
        Min_T.product_name AS "cheapest_product",
        Min_T.quantity AS "chp_qty"
    FROM T2 AS Max_T
    JOIN T2 AS Min_T
    ON Max_T.store_id = Min_T.store_id AND Min_T.price < Max_T.price AND Max_T.quantity < Min_T.quantity
)

SELECT 
    S.*,
    T3.most_exp_product,
    T3.cheapest_product,
    ROUND(T3.chp_qty / T3.exp_qty, 2) AS "imbalance_ratio"
FROM T3
JOIN stores AS S
ON T3.store_id = S.store_id
ORDER BY imbalance_ratio DESC, S.store_name