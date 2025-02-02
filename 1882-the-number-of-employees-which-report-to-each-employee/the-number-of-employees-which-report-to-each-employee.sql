# Write your MySQL query statement below
with temp as
(select reports_to, count(*) as reports_count,round(avg(age),0) as average_age
from employees
where reports_to is not Null
group by reports_to)
select a.reports_to as employee_id,b.name,a.reports_count,a.average_age
from temp a inner join employees b
on a.reports_to=b.employee_id
order by employee_id;
