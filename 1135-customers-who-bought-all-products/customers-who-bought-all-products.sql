# Write your MySQL query statement below
with temp as 
(select distinct customer_id,p.product_key
from customer c ,product p
where p.product_key=c.product_key)
select customer_id
from temp
group by customer_id
having count(distinct product_key)=(select count(distinct product_key) from product);
-- where product_key in (select distinct product_key from product);