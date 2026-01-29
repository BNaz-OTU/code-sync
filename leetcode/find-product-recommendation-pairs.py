# Write your MySQL query statement below

WITH T1 AS (
SELECT 
    FIR.product_id AS "product1_id", 
    SEC.product_id AS "product2_id", 
    COUNT(*) AS "customer_count"
FROM ProductPurchases AS FIR
JOIN ProductPurchases AS SEC
ON FIR.product_id < SEC.product_id AND FIR.user_id = SEC.user_id
GROUP BY FIR.product_id, SEC.product_id
)

SELECT
    T1.product1_id,
    T1.product2_id,
    P1.category AS "product1_category",
    P2.category AS "product2_category",
    T1.customer_count
FROM T1
JOIN ProductInfo AS P1
ON T1.product1_id = P1.product_id
JOIN ProductInfo AS P2
ON T1.product2_id = P2.product_id
WHERE T1.customer_count >= 3
ORDER BY T1.customer_count DESC, T1.product1_id ASC, T1.product2_id ASC