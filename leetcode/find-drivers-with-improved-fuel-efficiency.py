# Write your MySQL query statement below

-- Determine first half year trips and calculate fuel consumption averages
WITH FIRST_HALF AS (
    SELECT 
        *,
        AVG(distance_km / fuel_consumed) AS "first_half_avg"
    FROM trips
    WHERE MONTH(trip_date) <= 6
    GROUP BY driver_id
),

-- Determine second half year trips and calculate fuel consumption averages
SECOND_HALF AS (
    SELECT 
        *,
        AVG(distance_km / fuel_consumed) AS "second_half_avg"
    FROM trips
    WHERE MONTH(trip_date) > 6
    GROUP BY driver_id
),

-- Calculate fuel efficiency and filter for drivers that drove both halves of the year
CALC AS (
    SELECT 
        F.driver_id,
        ROUND(F.first_half_avg, 2) AS "first_half_avg",
        ROUND(S.second_half_avg, 2) AS "second_half_avg",
        ROUND(S.second_half_avg - F.first_half_avg, 2) AS "efficiency_improvement"
    FROM FIRST_HALF AS F
    JOIN SECOND_HALF AS S
    ON F.driver_id = S.driver_id
)

-- Filter for postive fuel efficiency and append the driver names
SELECT 
    D.*,
    C.first_half_avg,
    C.second_half_avg,
    C.efficiency_improvement
FROM CALC AS C
JOIN drivers AS D
ON C.driver_id = D.driver_id
WHERE efficiency_improvement > 0
ORDER BY efficiency_improvement DESC, D.driver_name ASC