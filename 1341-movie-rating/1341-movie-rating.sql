# Write your MySQL query statement below
(select t.name as results 
from
    (select *, count(user_id) as count_user_id
    from MovieRating join Users using(user_id)
    group by user_id
    order by count_user_id desc, name asc
    limit 1) as t)
union all
(select t2.title as results
from
    (select title, movie_id, avg(rating) as avg_rating
    from MovieRating join Movies using(movie_id)
    where substring(created_at, 1, 4) = 2020 and substring(created_at, 6, 2) = 02
    group by movie_id
    order by avg_rating desc, title asc
    limit 1) as t2)
