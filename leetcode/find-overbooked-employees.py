# Write your MySQL query statement below
-- FROM DISCUSSION (very helpful): https://leetcode.com/problems/find-overbooked-employees/description/comments/3118095/

-- ANOTHER METHOD: https://www.youtube.com/watch?v=jqLHMyfxDjw -- made an error, should use YEARWEEK instead of WEEK

WITH T1 AS (
    SELECT 
        *,
        YEARWEEK(meeting_date, 3) AS "year_week"
    FROM meetings
),

T2 AS (
    SELECT 
        employee_id, 
        year_week,
        SUM(duration_hours) AS "total_hours"
    FROM T1
    GROUP BY employee_id, year_week
)

SELECT
    E.*,
    COUNT(*) AS "meeting_heavy_weeks"
FROM T2 
JOIN employees AS E
ON T2.employee_id = E.employee_id
WHERE total_hours >= 20
GROUP BY E.employee_id
HAVING COUNT(*) >= 2
ORDER BY meeting_heavy_weeks DESC, employee_name

-- SELECT * FROM T2