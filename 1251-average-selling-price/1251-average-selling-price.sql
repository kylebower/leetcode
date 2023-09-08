# Write your MySQL query statement below
SELECT
    u.product_id,
    IF(SUM(u.units) IS NOT NULL, ROUND(SUM(u.units * p.price)/SUM(u.units), 2), 0) AS average_price
FROM
    UnitsSold u LEFT JOIN Prices p
    ON u.product_id = p.product_id AND (u.purchase_date BETWEEN p.start_date AND p.end_date)
GROUP BY
    product_id