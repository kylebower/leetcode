# Write your MySQL query statement below
with t as (select status, request_at
           from Trips
           where client_id not in (select users_id from Users where banned = 'Yes')
           and driver_id not in (select users_id from Users where banned = 'Yes'))
select request_at as Day,
       round(avg(t.status <> 'completed'), 2) as 'Cancellation Rate'
from t
where request_at between '2013-10-01' and '2013-10-03'
group by request_at