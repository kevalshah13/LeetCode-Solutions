# Write your MySQL query statement below
select b.product_name,a.year,a.price
from sales a inner join product b
on a.product_id=b.product_id;
