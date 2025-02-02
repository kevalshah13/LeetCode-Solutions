# Write your MySQL query statement below
with temp as
(select product_id,new_price as price,
change_Date,row_number() over(partition by product_id order by change_date desc) as r1
from products
where change_date<="2019-08-16")
select distinct p.product_id,coalesce(t.price,10) as price
from products p left join temp t
on p.product_id=t.product_id and t.r1=1
-- group by product_id
-- having r1=max(r1);
-- union all
-- select product_id,10 as price
-- from products
-- where product_id not in (select product_id from temp)

