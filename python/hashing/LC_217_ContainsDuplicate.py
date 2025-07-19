# https://leetcode.com/problems/contains-duplicate/
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False

sol = Solution()
assert sol.containsDuplicate([1,2,3,1]) == True
assert sol.containsDuplicate([1,2,3,4]) == False
assert sol.containsDuplicate( [1,1,1,3,3,4,3,2,4,2]) == True