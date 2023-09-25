# Write your MySQL query statement below
SELECT
    T.employee_id
FROM(
    (SELECT *
     FROM Employees e
     LEFT JOIN Salaries s
     USING(employee_id)
    )
    UNION
    (SELECT *
     FROM Employees e
     RIGHT JOIN Salaries s
     USING(employee_id)
    ))
    AS T
WHERE
    T.name IS NULL OR T.salary IS NULL
ORDER BY
    T.employee_id