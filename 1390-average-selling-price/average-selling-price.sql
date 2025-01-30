# Write your MySQL query statement below
-- with TotalUnit as 
-- (select sum(units) as total_units
-- from UnitsSold
-- group by product_id)
with agg as
(select p.product_id,units,price
from prices p left join unitsSold us
on p.product_id=us.product_id and p.start_date<=us.purchase_Date and us.purchase_date<=p.end_date)
select product_id,
round(coalesce(sum(price*units)/sum(units),0.0),2) as average_price
from agg
group by product_id;