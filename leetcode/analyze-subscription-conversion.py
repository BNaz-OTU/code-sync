# Write your MySQL query statement below

-- ANOTHER METHOD: https://leetcode.com/problems/analyze-subscription-conversion/solutions/7323232/simple-sql-without-cte-by-sarang_malpure-2ht4

WITH T1 AS (SELECT 
    user_id,
    ROUND(SUM(IF(activity_type = "free_trial", activity_duration, 0)) / COUNT(IF(activity_type = "free_trial", 1, 0)), 2) AS "trial_avg_duration",
    ROUND(SUM(IF(activity_type = "paid", activity_duration, 0)) / COUNT(IF(activity_type = "paid", 1, 0)), 2) AS "paid_avg_duration"
FROM UserActivity
GROUP BY user_id, activity_type
ORDER BY user_id ASC)

SELECT 
    tab1.user_id,
    tab1.trial_avg_duration,
    tab2.paid_avg_duration
FROM T1 AS tab1
JOIN T1 AS tab2
ON tab1.trial_avg_duration != 0 AND tab2.paid_avg_duration != 0 AND tab1.user_id = tab2.user_id