# Write your MySQL query statement below
SELECT
    u.product_id,
    ROUND(SUM(u.units * p.price)/SUM(u.units), 2) AS average_price
FROM
    UnitsSold u JOIN Prices p
    ON u.product_id = p.product_id AND (purchase_date BETWEEN start_date AND end_date)
GROUP BY
    product_id