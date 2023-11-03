# Write your MySQL query statement below
with T as (select *
            from Trips
            where client_id in (select users_id from Users where banned = 'No')
            and driver_id in (select users_id from Users where banned = 'No'))
select request_at as day,
    round(1 - avg(t.status = 'completed'), 2) as 'Cancellation Rate'
from T
where '2013-10-01' <= request_at and request_at <= '2013-10-03'
group by request_at