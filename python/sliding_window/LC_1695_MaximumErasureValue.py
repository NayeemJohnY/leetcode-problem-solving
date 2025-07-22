# https://leetcode.com/problems/maximum-erasure-value
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sub_array = set()
        left = right = curr_sum = max_sum = 0
        while right < len(nums):
            if nums[right] not in sub_array:
                sub_array.add(nums[right])
                curr_sum += nums[right]
                max_sum = max(max_sum, curr_sum)
                right += 1
            else:
                sub_array.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
        return max_sum
