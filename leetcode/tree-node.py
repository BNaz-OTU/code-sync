# Write your MySQL query statement below

-- ANOTHER METHOD: https://www.youtube.com/watch?v=-hHUVAlTwZg
-- ANOTHER METHOD: https://www.youtube.com/watch?v=jfE0d4hR--s

SELECT 
    T1.id, 
    CASE
        WHEN COUNT(T1.p_id) = 0 THEN "Root"
        WHEN COUNT(T2.p_id) = 0 THEN "Leaf"
        ELSE "Inner"
    END AS "type"
FROM TREE AS T1
LEFT JOIN TREE AS T2
ON T1.id = T2.p_id
GROUP BY T1.id