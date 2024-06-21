# Write your MySQL query statement below
SELECT 
    ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) as fraction
FROM 
    Activity
WHERE 
    (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
    IN 
    (
        -- Subquery: Players and their first login date
        SELECT 
            player_id,
            MIN(event_date) AS first_login
        FROM 
            Activity
        GROUP BY 
            player_id
    );
-- with table1 as
-- (select player_id,event_date, lag(event_date) over(order by event_date) as prev_date,
-- dense_rank() over(partition by player_id order by event_date) as ro
-- from activity)
-- select Round(sum(case when (event_date-prev_date=1 or prev_Date is Null) and ro=2 then 1 else 0 end)/count(distinct player_id),2) as fraction
-- from table1

