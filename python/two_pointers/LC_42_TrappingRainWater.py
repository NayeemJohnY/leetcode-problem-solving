# https://leetcode.com/problems/trapping-rain-water
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_trap = 0
        while (left < right):
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_trap += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_trap += right_max - height[right]

        return total_trap
