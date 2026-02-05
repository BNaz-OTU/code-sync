# Write your MySQL query statement below

-- USED SOLN: https://www.youtube.com/watch?v=l8d1ps_WVz4

WITH CTE AS (SELECT 
    user_id,
    reaction,
    COUNT(DISTINCT content_id) AS "num"
FROM reactions
GROUP BY user_id, reaction),

CTE2 AS (
    SELECT *,
    SUM(num) OVER(PARTITION BY user_id) AS "content_reactions",
    ROUND(num / SUM(num) OVER(PARTITION BY user_id), 2) AS "reaction_ratio",
    ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY num DESC) AS "rnk"
    FROM CTE
)

SELECT 
    user_id,
    reaction AS "dominant_reaction",
    reaction_ratio
FROM CTE2
WHERE content_reactions >= 5
AND reaction_ratio >= 0.6
AND rnk= 1
ORDER BY reaction_ratio DESC, user_id ASC