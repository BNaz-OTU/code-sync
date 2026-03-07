# Write your MySQL query statement below

-- Group together the weeks of each year
WITH T1 AS (
    SELECT
        *,
        YEARWEEK(meeting_date, 3) AS year_week
    FROM meetings
),

-- Calculate the total hours of meeting time in a week
T2 AS (
    SELECT 
        employee_id, 
        year_week,
        SUM(duration_hours) AS "total_hours"
    FROM T1
    GROUP BY employee_id, year_week
)

-- Apply the filters
SELECT
    E.*,
    COUNT(*) AS "meeting_heavy_weeks"
FROM T2
JOIN employees AS E
ON T2.employee_id = E.employee_id
WHERE total_hours > 20
GROUP BY E.employee_id
HAVING COUNT(*) > 1
ORDER BY meeting_heavy_weeks DESC, E.employee_name