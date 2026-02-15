# Write your MySQL query statement below

-- Filter for entries that are less than the minimum of 3
WITH T1 AS(
    SELECT employee_id
    FROM performance_reviews
    GROUP BY employee_id 
    HAVING COUNT(*) > 2
),

-- Set up ranking to easily identify the most recent entries to the Table of a user
T2 AS (
    SELECT *, dense_rank()
    OVER (PARTITION BY employee_id ORDER BY review_date DESC) AS "Ranked"
    FROM performance_reviews
),

-- USE "T1" to filter the modified table
T3 AS (
    SELECT T2.*
    FROM T2
    JOIN T1
    ON T1.employee_id = T2.employee_id
    WHERE Ranked <= 3 
),

-- Set up ranking to easily locate if improvements were being made each time per employee
T4 AS (
    SELECT *, dense_rank()
    OVER (PARTITION BY employee_id ORDER BY rating DESC) AS "Improve"
    FROM T3
)

-- Using the "Ranked" ranking and "Improve" ranking, check to make sure they are the same number
-- this will identify if improvements were made with each new recent entry, if they are different then an improvement wasn't made
-- and will be filtered out. Also check to make sure that there are still 3 entries, since some entries would be removed
-- if they didn't have the same "Ranked" ranking and "Improve" ranking, if there aren't 3 remove those.
SELECT 
    E.employee_id,
    E.name, 
    (MAX(T4.rating) - MIN(T4.rating)) AS "improvement_score"
FROM T4
JOIN employees AS E
ON T4.employee_id = E.employee_id
WHERE T4.Ranked = T4.Improve
GROUP BY T4.employee_id
HAVING COUNT(*) = 3
ORDER BY improvement_score DESC, E.name ASC