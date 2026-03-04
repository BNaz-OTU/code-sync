# Write your MySQL query statement below
-- USED SOLN: https://www.youtube.com/watch?v=AUYkIomulaw

-- User name
WITH T1 AS (
    SELECT 
        user_id,
        name,
        COUNT(*) AS "count_m"
    FROM Users JOIN MovieRating USING(user_id)
    GROUP BY user_id, name
    ORDER BY count_m DESC, name ASC
    LIMIT 1
),

users AS (
SELECT 
    name AS "results"
FROM T1
),
-- Movie name
T2 AS (
    SELECT
        movie_id,
        title,
        AVG(rating) AS "count_a"
    FROM Movies
    JOIN MovieRating USING(movie_id)
    WHERE created_at BETWEEN "2020-02-01" AND "2020-02-29"
    GROUP BY movie_id, title
    ORDER BY count_a DESC, title ASC
    LIMIT 1
),

movies AS (
    SELECT 
        title AS "results"
    FROM T2
)

SELECT * FROM users
UNION ALL
SELECT * FROM movies