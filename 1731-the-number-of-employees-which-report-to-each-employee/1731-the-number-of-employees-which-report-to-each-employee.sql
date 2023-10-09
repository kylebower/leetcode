# Write your MySQL query statement below
SELECT
    E1.reports_to AS employee_id,
    E2.name AS name,
    COUNT(E2.employee_id) AS reports_count,
    ROUND(AVG(E1.age), 0) AS average_age
FROM
    Employees E1 JOIN Employees E2 ON E1.reports_to = E2.employee_id
GROUP BY
    E1.reports_to
ORDER BY
    E2.employee_id