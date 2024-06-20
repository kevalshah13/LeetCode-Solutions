# Write your MySQL query statement below
select Round(sum(case when order_date=customer_pref_delivery_date then 1 else 0 end)*100/count(*),2) as immediate_percentage
from(
    select *,row_number() over(partition by customer_id order by order_date) as Orders
    from delivery) a
where Orders=1
