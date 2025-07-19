# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, sum, minLen = 0, 0, float("inf")
        for end in range(len(nums)):
            sum += nums[end]
            while sum >= target:
                minLen = min(minLen, end-start+1)
                sum -= nums[start]
                start += 1
        return minLen if minLen != float("inf") else 0

sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
print(sol.minSubArrayLen(4, [1, 1, 3, 2]))
print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))