# Write your MySQL query statement below

SELECT 
    customer_id
    -- SUM(IF(transaction_type = "refund", 1, 0)) AS "refunds",
    -- COUNT(transaction_type) AS "transactions",
    -- DATEDIFF(MAX(transaction_date), MIN(transaction_date)) AS "Loyalty"

FROM customer_transactions
GROUP BY customer_id
HAVING 
    COUNT(*) >= 3 AND 
    SUM(IF(transaction_type = "refund", 1, 0)) / COUNT(transaction_type) < 0.2 AND 
    DATEDIFF(MAX(transaction_date), MIN(transaction_date)) >= 30