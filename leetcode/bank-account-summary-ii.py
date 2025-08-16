# Write your MySQL query statement below

SELECT 
    U.name AS 'NAME', 
    SUM(T.amount) AS 'BALANCE'
FROM Users AS U
LEFT JOIN Transactions AS T
ON U.account = T.account
GROUP BY U.account
HAVING SUM(T.amount) > 10000