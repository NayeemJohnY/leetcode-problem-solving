-- https://leetcode.com/problems/sales-person/
select DISTINCT SalesPerson.name from SalesPerson
left join orders
on orders.sales_id  = SalesPerson.sales_id
where SalesPerson.sales_id not in (select orders.sales_id from orders
join company
on company.com_id = orders.com_id
where company.name = "RED" )