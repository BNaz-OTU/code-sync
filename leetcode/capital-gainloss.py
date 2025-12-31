# Write your MySQL query statement below

WITH T1 AS (SELECT 
    stock_name,
    SUM(IF(operation = "Buy", price, 0)) AS "total_buy",
    SUM(IF(operation = "Sell", price, 0)) AS "total_loss"
FROM Stocks
GROUP BY stock_name)

SELECT
    stock_name,
    (total_loss - total_buy) AS "capital_gain_loss"
FROM T1