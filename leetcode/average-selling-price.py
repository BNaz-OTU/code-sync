# Write your MySQL query statement below

SELECT 
    P.product_id,
    IFNULL(ROUND(SUM(P.price * U.units)/ SUM(U.units), 2), 0) AS "average_price"
FROM Prices AS P
LEFT JOIN UnitsSold AS U
ON (U.purchase_date BETWEEN P.start_date AND P.end_date) AND (P.product_id = U.product_id)
GROUP BY P.product_id