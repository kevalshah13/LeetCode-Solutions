# Write your MySQL query statement below
-- select concat(year(trans_date),'-',date_format(trans_Date,'%m')) as month,
select date_format(trans_Date,'%Y-%m') as month,
        country,
        count(*) as trans_count,
        sum(case when state='approved' then 1 else 0 end) as approved_Count,
        sum(amount) as trans_total_amount,
        sum(case when state='approved' then amount else 0 end) as approved_total_amount
from transactions
group by month,country;
