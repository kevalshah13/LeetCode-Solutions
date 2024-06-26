# Write your MySQL query statement below
select product_id, first_year, quantity, price
from (
select b.product_id, a.year as first_year, a.quantity, a.price,rank() over(partition by a.product_id order by a.year) as r
from sales a inner join product b
on a.product_id=b.product_id) bc
where r=1