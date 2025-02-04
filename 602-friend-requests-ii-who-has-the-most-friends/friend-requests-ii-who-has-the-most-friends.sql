# Write your MySQL query statement below
with friends as
(select requester_id,accepter_id
from requestaccepted  
union all 
select accepter_id as requester_id,requester_id as accepter_id
from requestaccepted)
select requester_id as id,count(distinct accepter_id) as num
from friends
group by requester_id
order by num desc
limit 1;
