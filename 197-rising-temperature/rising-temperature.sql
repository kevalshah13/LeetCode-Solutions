# Write your MySQL query statement below
-- with lag_info as
-- (select id,recordDate,lag(recordDate) over(order by recordDate) as prev_date,
-- temperature, lag(recordDate) over(order by recordDate) as prev_temp
-- from weather)
-- select id
-- from lag_info
-- where timestampdiff(day,recordDate,prev_date)=1 and temperature>prev_temp;

SELECT 
    w1.id
FROM 
    Weather w1
JOIN 
    Weather w2
ON 
    DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE 
    w1.temperature > w2.temperature;