# Write your MySQL query statement below

WITH T1 AS(
    SELECT employee_id
    FROM performance_reviews
    GROUP BY employee_id 
    HAVING COUNT(*) > 2
),

T2 AS (
    SELECT *, dense_rank()
    OVER (PARTITION BY employee_id ORDER BY review_date DESC) AS "Ranked"
    FROM performance_reviews
),

T3 AS (
    SELECT T2.*
    FROM T2
    JOIN T1
    ON T1.employee_id = T2.employee_id
    WHERE Ranked <= 3 
),

T4 AS (
    SELECT *, dense_rank()
    OVER (PARTITION BY employee_id ORDER BY rating DESC) AS "Improve"
    FROM T3
)

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