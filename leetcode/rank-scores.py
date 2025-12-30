# Write your MySQL query statement below

-- USED SOLN: https://www.youtube.com/watch?v=rnaohD9aU_Y

SELECT 
    score, 
    dense_rank() 
OVER (ORDER BY score DESC) AS "rank"
FROM Scores
-- ORDER BY score