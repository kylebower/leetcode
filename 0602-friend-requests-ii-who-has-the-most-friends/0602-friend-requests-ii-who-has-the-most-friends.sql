# Write your MySQL query statement below
SELECT T.id,
    COUNT(T.id) AS num
FROM
(SELECT
    requester_id  AS id
FROM
    RequestAccepted
UNION ALL
SELECT
    accepter_id AS id
FROM
    RequestAccepted) AS T
GROUP BY
    T.id
ORDER BY
    num DESC
LIMIT 1