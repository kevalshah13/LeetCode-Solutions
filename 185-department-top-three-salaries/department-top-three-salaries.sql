# Write your MySQL query statement below
with top_salary as
(select name,salary,departmentId,dense_rank() over(partition by departmentId order by salary desc) as r1
from employee
order by departmentId,r1
)
select b.name as department,
        a.name as employee,
        a.salary
from top_salary a inner join department b
on a.departmentId=b.id
where r1<=3
;