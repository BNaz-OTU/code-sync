# Write your MySQL query statement below

WITH T1 AS (SELECT *
FROM Students AS STU
CROSS JOIN Subjects AS SUB)

SELECT
    T1.student_id, 
    T1.student_name, 
    T1.subject_name,
    IFNULL(COUNT(E.subject_name), 0) AS "attended_exams"
FROM T1
LEFT JOIN Examinations AS E
ON T1.student_id = E.student_id AND T1.subject_name = E.subject_name
-- WHERE T1.student_name = "Bob"
GROUP BY T1.student_id, T1.student_name, T1.subject_name
ORDER BY T1.student_id ASC, T1.subject_name ASC