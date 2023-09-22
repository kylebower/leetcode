# Write your MySQL query statement below
SELECT *
FROM
    Users u
WHERE
    u.mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$' 