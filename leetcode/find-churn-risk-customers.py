# Write your MySQL query statement below
-- USED SOLN: https://www.youtube.com/watch?v=mSQx0QDmRWg

WITH T1 AS (
    SELECT *,
        ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY event_date DESC) AS "rnk"
    FROM subscription_events
),

T2 AS (
    SELECT 
        user_id,
        MAX(CASE WHEN rnk = 1 THEN plan_name ELSE NULL END) AS "current_plan",
        SUM(CASE WHEN rnk = 1 THEN monthly_amount ELSE 0 END) AS "current_monthly_amount",
        MAX(monthly_amount) AS "max_historical_amount",
        DATEDIFF(MAX(event_date), MIN(event_date)) AS "days_as_subscriber"
    FROM T1
    GROUP BY user_id
)


SELECT *
FROM T2
WHERE 
    (current_plan IS NOT NULL) AND
    (days_as_subscriber >= 60) AND
    ((max_historical_amount * 0.5) > current_monthly_amount)
ORDER BY days_as_subscriber DESC, user_id ASC