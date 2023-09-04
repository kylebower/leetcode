# Write your MySQL query statement below
SELECT
    p.product_name, 
    s.year,
    s.price
FROM
    Sales s INNER JOIN Product AS p
    USING(product_id)
GROUP BY
    sale_id