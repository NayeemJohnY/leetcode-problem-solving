-- https://leetcode.com/problems/employee-bonus/
SELECT a.player_id, MIN(a.event_date) as first_login FROM Activity a
group by a.player_id