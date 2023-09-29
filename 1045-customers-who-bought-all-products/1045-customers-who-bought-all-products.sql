# Write your MySQL query statement below
SELECT
    customer_id
FROM
    Customer c
GROUP BY
    customer_id
HAVING
    COUNT(DISTINCT c.product_key) = (SELECT COUNT(DISTINCT p.product_key) FROM Product p)