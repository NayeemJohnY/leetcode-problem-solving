-- https://leetcode.com/problems/employees-earning-more-than-their-managers
select e.name as Employee from employee e
join employee m
on m.Id = e.managerId
where e.salary > m.salary


-- select e.name as Employee from employee e
-- where salary > (
--     select m.salary from Employee m where m.managerId is NULL
--     AND e.managerId = m.id)