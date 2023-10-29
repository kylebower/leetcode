# Write your MySQL query statement below
with base as
(select visited_on,
 sum(amount) as amount
from Customer
group by visited_on
)

select b1.visited_on,
    round(sum(b2.amount), 2) as amount,
    round(sum(b2.amount)/7, 2) as average_amount
from base b1
join base b2 on datediff(b1.visited_on, b2.visited_on) between 0 and 6
group by visited_on
having count(distinct b2.visited_on) = 7
order by visited_on asc