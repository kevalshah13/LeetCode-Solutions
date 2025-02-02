# Write your MySQL query statement below
with temp as
(select employee_id,department_id
from employee
where primary_flag='Y'),
temp1 as
(select employee_id,department_id
from employee 
where employee_id not in (select employee_id from temp))
select *
from temp
union
select *
from temp1;