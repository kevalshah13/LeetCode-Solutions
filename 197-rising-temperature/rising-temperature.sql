# Write your MySQL query statement below
with table1 as
(select id,temperature-lag(temperature,1,Null) over(order by recordDate) as diff_temp,
datediff(recordDate,lag(recordDate) over(order by recordDate)) as date_diff
from weather)
select id
from table1 
where diff_temp>0 and date_diff=1
-- where <temperature