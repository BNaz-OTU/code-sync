# Write your MySQL query statement below

-- SWAP one half of the numbers
WITH T1 AS (SELECT 
    S1.id,
    S2.student
FROM Seat AS S1
LEFT JOIN Seat AS S2
ON (S1.id % 2 = 1) AND S1.id = S2.id - 1
WHERE S2.id IS NOT NULL),

-- Swap the other half of the numbers
T2 AS (
SELECT 
    S1.id, 
    S2.student
FROM Seat AS S1
LEFT JOIN Seat AS S2
ON (S1.id % 2 = 0) AND S1.id = S2.id + 1
WHERE S2.id IS NOT NULL),

-- Combine the 2 tables with swapped id's
T3 AS (SELECT *
FROM T2

UNION 

SELECT *
FROM T1
),

-- Reorder the tables in ascending order
T4 AS (
    SELECT *
    FROM T3
    ORDER BY T3.id
),

-- Get last value in OG table
T5 AS (SELECT *
FROM Seat
ORDER BY id DESC 
LIMIT 1),

-- IF the id is ODD keep it, otherwise don't implement it
T6 AS (

SELECT *
FROM T4

UNION

SELECT *
FROM T5
WHERE id % 2 = 1
)

-- Return the final table ordered
SELECT *
FROM T6 
ORDER BY id