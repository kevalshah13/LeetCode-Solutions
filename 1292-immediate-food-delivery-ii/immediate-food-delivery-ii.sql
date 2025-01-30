# Write your MySQL query statement below
with first_orders as
(select order_date,
customer_pref_delivery_date,
rank() over(partition by customer_id order by order_Date) as ranked
from delivery)
select 
Round(sum(case when Timestampdiff(day,order_date,customer_pref_delivery_date)=0 then 1 else 0 end)*100.0/count(*),2) as immediate_percentage
from first_orders
where ranked=1;