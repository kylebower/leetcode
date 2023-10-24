# Write your MySQL query statement below
select t.id, t.visit_date, t.people
from (select *, 
      lead(people,1) over (order by id) as nxt, 
      lead(people,2) over (order by id) as nxt2, 
      lag(people,1) over (order by id) as pre, 
      lag(people,2) over (order by id) as pre2
      from Stadium) as t
where t.people >= 100 and ((t.nxt >= 100 and (t.nxt2 >= 100 or t.pre >= 100)) or (t.pre >= 100 and t.pre2 >= 100))