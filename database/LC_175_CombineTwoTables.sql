-- https://leetcode.com/problems/combine-two-tables
select firstName, lastName, city, state
from person
left join address
on address.personId = person.personId