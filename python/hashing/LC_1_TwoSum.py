# https://leetcode.com/problems/two-sum/description/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                return [map.get(diff), i]
            map[nums[i]] = i
        return []
    
sol = Solution()
assert sol.twoSum([2,7,11,15], 9) == [0, 1]
assert sol.twoSum([3,2,4], 6) == [1, 2]
assert sol.twoSum([3,3], 6) == [0, 1]