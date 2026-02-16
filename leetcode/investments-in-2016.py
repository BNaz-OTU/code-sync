# Write your MySQL query statement below

-- Check to find multiple policy holders with same 'tiv_2015' value
WITH T1 AS (
    SELECT 
        tiv_2015, 
        COUNT(*) AS "Num_holders"
    FROM Insurance
    GROUP BY tiv_2015
),

-- Check to find only one unique (lat, lon) pair
T2 AS (
    SELECT 
        lat,
        lon, 
        COUNT(*) AS "Unique_loc"
    FROM Insurance 
    GROUP BY lat, lon
),

-- Combine the Insurance table and the multiple policy holders table
T3 AS (
    SELECT 
        I.*, 
        T1.Num_holders
    FROM Insurance AS I
    JOIN T1
    ON I.tiv_2015 = T1.tiv_2015
)

-- Combine the previous table and the unique location table, then begin filtering to get the answer
SELECT 
    ROUND(SUM(T3.tiv_2016), 2) AS "tiv_2016"
FROM T3
JOIN T2
ON T3.lat = T2.lat AND T3.lon = T2.lon
WHERE T2.Unique_loc = 1 AND T3.Num_holders > 1