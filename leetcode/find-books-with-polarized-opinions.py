# Write your MySQL query statement below
-- USED SOLN: https://www.youtube.com/watch?v=RSN38-ypuRI

WITH T1 AS (
    SELECT
        book_id,
        MAX(session_rating) - MIN(session_rating) AS "rating_spread",
        ROUND(SUM(CASE WHEN session_rating <= 2 OR session_rating >= 4 THEN 1 ELSE 0 END) / COUNT(session_rating), 2) AS "polarization_score",
        SUM(CASE WHEN session_rating <= 2 THEN 1 ELSE 0 END) AS "two_less",
        SUM(CASE WHEN session_rating >= 4 THEN 1 ELSE 0 END) AS "four_more"
    FROM reading_sessions
    GROUP BY book_id
    HAVING COUNT(*) >= 5
)

SELECT 
    B.*,
    T1.rating_spread,
    T1.polarization_score
FROM T1
JOIN books AS B
ON T1.book_id = B.book_id
WHERE T1.two_less > 0 AND T1.four_more > 0 AND T1.polarization_score >= 0.6
ORDER BY T1.polarization_score DESC, B.title DESC