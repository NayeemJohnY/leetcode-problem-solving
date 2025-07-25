# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique = set()
        max_sum = 0
        max_ele = float("-inf")
        for num in nums:
            if num >= 0 and num not in unique:
                max_sum += num
                unique.add(num)
            elif num < 0 and not unique:
                max_ele = max(num, max_ele)

        return max_sum if unique else max_ele
