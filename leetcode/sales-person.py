# Write your MySQL query statement below

WITH T1 AS (SELECT S.sales_id
FROM Orders AS O
JOIN Company AS C
ON O.com_id = C.com_id
JOIN SalesPerson AS S
ON O.sales_id = S.sales_id
WHERE C.name = "RED")

SELECT SP.name
FROM SalesPerson AS SP
LEFT JOIN T1
ON SP.sales_id = T1.sales_id
WHERE T1.sales_id IS NULL