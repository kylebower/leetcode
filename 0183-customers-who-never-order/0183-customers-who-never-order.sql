# Write your MySQL query statement below
SELECT Customers.name as "Customers"
FROM Customers
WHERE Customers.id NOT IN(SELECT customerId FROM Orders);