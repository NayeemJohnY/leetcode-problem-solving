-- https://leetcode.com/problems/triangle-judgement/
select *, 
case 
when x + y > z AND y+z > x AND x+z > y Then "Yes"
else "No"
END as triangle
from Triangle