# Write your MySQL query statement below
(select b.name as results
from movieRating a inner join users b
on a.user_id=b.user_id
group by a.user_id
order by count(*) desc,b.name
limit 1)
union all
(select b.title as results
from movieRating a inner join movies b
on a.movie_id=b.movie_id
where month(created_at)=2 and year(created_at)=2020
group by a.movie_id
order by avg(rating) desc,title
limit 1);