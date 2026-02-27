# Write your MySQL query statement below
WITH T1 AS (
    SELECT 
        *,
        ROW_NUMBER() OVER(PARTITION BY student_id, subject ORDER BY exam_date DESC) AS "latest_date",
        ROW_NUMBER() OVER(PARTITION BY student_id, subject ORDER BY exam_date) AS "first_date"
    FROM Scores
),

T2 AS (
    SELECT 
        student_id,
        subject,
        MAX(CASE WHEN first_date = 1 THEN score ELSE NULL END) AS "first_score",
        MAX(CASE WHEN latest_date = 1 THEN score ELSE NULL END) AS "latest_score"
    FROM T1
    GROUP BY student_id, subject
    HAVING COUNT(*) > 1
)

SELECT *
FROM T2
WHERE latest_score > first_score
ORDER BY student_id, subject