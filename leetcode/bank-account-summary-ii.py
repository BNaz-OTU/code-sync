# Write your MySQL query statement below

SELECT U.name AS "NAME", SUM(amount) AS "BALANCE"
FROM Users AS U
JOIN Transactions AS T
ON U.account = T.account
GROUP BY U.account
HAVING SUM(amount) > 10000