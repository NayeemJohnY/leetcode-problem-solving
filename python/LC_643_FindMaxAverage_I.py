# https://leetcode.com/problems/maximum-average-subarray-i/
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[0:k])
        maxSum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            if (current_sum > maxSum):
                maxSum = current_sum
        return maxSum/k


sol = Solution()
assert sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75000
assert sol.findMaxAverage([5], 1) == 5.00000

