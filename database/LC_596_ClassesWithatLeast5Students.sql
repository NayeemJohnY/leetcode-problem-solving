-- https://leetcode.com/problems/classes-with-at-least-5-students/
select class from courses
group by class
having count(student) >= 5