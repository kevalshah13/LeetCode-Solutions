# Write your MySQL query statement below
select query_name, Round(avg(rating/position),2) as quality,
Round(sum(case when rating<3 then 1 else 0 end)*100/count(*),2) as poor_query_percentage
from queries
where query_name is not Null
group by query_name;
-- having query_name!=null