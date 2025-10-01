-- https://leetcode.com/problems/employee-bonus/
select name, bonus from employee
left join bonus
on employee.empId = bonus.empId
where bonus < 1000 OR bonus is NULL