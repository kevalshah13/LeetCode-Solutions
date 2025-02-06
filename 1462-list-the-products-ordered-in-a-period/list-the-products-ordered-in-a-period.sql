# Write your MySQL query statement below
select a.product_name,sum(b.unit) as unit
from products a inner join orders b
on a.product_id=b.product_id
where month(b.order_date)=2 and year(b.order_date)=2020
group by b.product_id
having sum(b.unit)>=100;
