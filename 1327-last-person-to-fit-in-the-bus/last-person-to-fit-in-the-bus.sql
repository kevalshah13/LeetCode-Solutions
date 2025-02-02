-- Write your PostgreSQL query statement below
with cte as (select * , 
sum(weight) over (order by turn) as rolling_weight
from queue)
select person_name from cte where rolling_weight <= 1000
order by rolling_weight desc
limit 1;