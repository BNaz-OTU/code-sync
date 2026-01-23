# Write your MySQL query statement below

-- The "RequestAccepted" Table is full of accepted friend requests. Column "requester_id" signifies a person SENDING a friend request that was accepted
-- and the column "accepter_id" signifes a person RECEIVING and accepting the friend request. There are no duplicates in the "RequestAccepted" table.
-- To get the answer, just add the requests SENT by a user and add the requests a user RECEIVED, afterwards combine both SENT and RECEIVED for the final answer.

WITH T1 AS (
    -- RECEIVED accepted friend requests
    SELECT 
        accepter_id
    FROM RequestAccepted 

    UNION ALL

    -- SENT accepted friend requests
    SELECT 
        requester_id 
    FROM RequestAccepted
)

SELECT 
    accepter_id AS "id",
    COUNT(*) AS "num"
FROM T1
GROUP BY accepter_id
ORDER BY num DESC
LIMIT 1