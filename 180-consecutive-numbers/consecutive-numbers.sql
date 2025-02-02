# Write your MySQL query statement below
with temp as
(select id,num,lead(num) over(order by id) as num2
from logs),
temp1 as
(select distinct id,num,num2,lead(num2) over(order by id) as num3
from temp)
select distinct num as ConsecutiveNums
from temp1
where num=num2 and num2=num3;
-- where a.num=b.num and b.num=c.num;
