# Write your MySQL query statement below

WITH T1 AS (
    SELECT 
        *,
        AVG(distance_km / fuel_consumed) AS "first_half_avg"
    FROM trips
    WHERE MONTH(trip_date) <= 6
    GROUP BY driver_id
),

T2 AS (
    SELECT 
        *,
        AVG(distance_km / fuel_consumed) AS "second_half_avg"
    FROM trips
    WHERE MONTH(trip_date) > 6
    GROUP BY driver_id
),

T3 AS (
SELECT 
    T1.driver_id,
    D.driver_name,
    ROUND(T1.first_half_avg, 2) AS "first_half_avg",
    ROUND(T2.second_half_avg, 2) AS "second_half_avg",
    ROUND(T2.second_half_avg - T1.first_half_avg, 2) AS "efficiency_improvement"
FROM T2
JOIN T1
ON T1.driver_id = T2.driver_id
JOIN drivers AS D
ON T1.driver_id = D.driver_id
ORDER BY efficiency_improvement DESC, D.driver_name 
)

SELECT *
FROM T3
WHERE efficiency_improvement > 0