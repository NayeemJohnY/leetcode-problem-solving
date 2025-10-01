-- https://leetcode.com/problems/customers-who-never-order/
select name as Customers from Customers
left join orders
on orders.customerId = Customers.id
where orders.id is null