# Write your MySQL query statement below

select distinct t.num as ConsecutiveNums
from
    (select num,
        lead(num,1) over (order by id) as nxt,
        lead(num,2) over (order by id) as nxt2
    from Logs l) as t
where t.num = t.nxt and t.num = t.nxt2