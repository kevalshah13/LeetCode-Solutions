# Write your MySQL query statement below
-- with temp as
-- (select player_id, 
-- event_date,
-- timestampdiff(day,event_date,lag(event_date) over(order by event_date)) as ddiff
-- from activity 
-- group by player_id
-- having event_date=min(event_date) and ddiff=1)
-- select Round(count(*)/(select count(distinct player_id) from activity),2) as fraction
-- from temp;

SELECT
  ROUND(
    COUNT(A1.player_id)
    / (SELECT COUNT(DISTINCT A3.player_id) FROM Activity A3)
  , 2) AS fraction
FROM
  Activity A1
WHERE
  (A1.player_id, DATE_SUB(A1.event_date, INTERVAL 1 DAY)) IN (
    SELECT
      A2.player_id,
      MIN(A2.event_date)
    FROM
      Activity A2
    GROUP BY
      A2.player_id
  );