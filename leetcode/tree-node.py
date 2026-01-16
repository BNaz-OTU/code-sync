# Write your MySQL query statement below

-- SELECT
--     id,
--     CASE
--         WHEN p_id IS NULL THEN "Root"
--         WHEN COUNT(DISTINCT p_id) > COUNT(id) THEN "Inner"
--         ELSE "Leaf"
--     END AS "type"
-- FROM Tree

SELECT 
    T1.id, 
    CASE
        WHEN COUNT(T1.p_id) = 0 THEN "Root"
        WHEN COUNT(T2.p_id) = 0 THEN "Leaf"
        ELSE "Inner"
    END AS "type"
    -- COUNT(T1.p_id) AS "A",
    -- COUNT(T2.p_id) AS "B"
FROM TREE AS T1
LEFT JOIN TREE AS T2
ON T1.id = T2.p_id
GROUP BY T1.id