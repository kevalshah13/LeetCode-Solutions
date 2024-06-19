# Write your MySQL query statement below
select machine_id, round(avg(tdiff),3) as processing_time
from 
(
    select machine_id,process_id, coalesce(timestamp-lag(timestamp,1,Null) over(partition by machine_id,process_id order by machine_id, process_id ,activity_type asc),0) as tdiff
from activity
) a
where tdiff!=0
group by machine_id