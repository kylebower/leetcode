# Write your MySQL query statement below
SELECT
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM
    Insurance A
WHERE
    (SELECT COUNT(*) FROM Insurance B WHERE A.lat = B.lat AND A.lon = B.lon) = 1
AND
    (SELECT COUNT(*) FROM Insurance C WHERE A.tiv_2015 = C.tiv_2015) > 1