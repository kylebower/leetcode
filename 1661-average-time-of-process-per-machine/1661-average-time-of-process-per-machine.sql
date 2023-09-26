# Write your MySQL query statement below
SELECT
    a.machine_id,
    ROUND((SELECT AVG(a1.timestamp) FROM Activity a1 WHERE activity_type = 'end' AND a1.machine_id = a.machine_id) - 
          (SELECT AVG(a1.timestamp) FROM Activity a1 WHERE activity_type = 'start' AND a1.machine_id = a.machine_id), 3)
          AS processing_time
FROM
    Activity a
GROUP BY
    a.machine_id