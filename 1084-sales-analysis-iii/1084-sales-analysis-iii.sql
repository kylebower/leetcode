# Write your MySQL query statement below
select t.product_id, t.product_name
from 
    (select *
    from Sales join Product using (product_id)) as t
group by product_id
having min(t.sale_date) >= '2019-01-01' and max(t.sale_date) <= '2019-03-31'