# Write your MySQL query statement below

SELECT 
    U.name, 
    IF(SUM(R.distance) IS NULL, 0, SUM(R.distance)) AS 'travelled_distance'
FROM Users AS U
LEFT JOIN Rides AS R
ON U.id = R.user_id
GROUP BY U.id
ORDER BY travelled_distance DESC, U.name ASC