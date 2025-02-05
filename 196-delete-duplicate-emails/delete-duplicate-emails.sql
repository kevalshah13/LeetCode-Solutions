# Write your MySQL query statement below
delete from person
where id not in 
(select min_id 
from 
(select min(Id) as min_id
from person
group by Email) as a)