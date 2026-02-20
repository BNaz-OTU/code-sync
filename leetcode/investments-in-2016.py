# Write your MySQL query statement below
WITH T1 AS (
    SELECT
        tiv_2015,
        COUNT(*) AS "num_holders"
    FROM Insurance
    GROUP BY tiv_2015
),

T2 AS (
    SELECT 
        lat,
        lon,
        COUNT(*) AS "unique_loc"
    FROM Insurance
    GROUP BY lat, lon
)

SELECT 
    ROUND(SUM(tiv_2016), 2) AS "tiv_2016"
FROM Insurance AS I
JOIN T1 
ON I.tiv_2015 = T1.tiv_2015
JOIN T2
ON I.lat = T2.lat and I.lon = T2.lon
WHERE (T1.num_holders > 1) AND (T2.unique_loc = 1)