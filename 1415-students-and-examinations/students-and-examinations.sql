# Write your MySQL query statement below

select s.student_id,student_name,su.subject_name,count(e.student_id) as attended_exams
from students s cross join subjects su
left join examinations e
on su.subject_name=e.subject_name and s.student_id=e.student_id
group by s.student_id,su.subject_name
order by s.student_id,su.subject_name;
-- select distinct st.student_id,student_name, s.subject_name, 
-- coalesce(count(*),0) as attended_exams
-- from examinations e cross join subjects s
-- -- on e.subject_name=s.subject_name
-- cross join students st
-- -- on st.student_id=e.student_id
-- group by st.student_id,s.subject_name
-- order by st.student_id,s.subject_name;