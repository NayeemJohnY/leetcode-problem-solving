# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List

# 1 2 3 4 5
# a[0] < a[end]
# 5 1 2 3 4
# a[0] > a[end]
# a[1] > a[end]
# 4 5 1 2 3
# 3 4 5 1 2
# 2 3 4 5 1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = left + (right - left ) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

sol = Solution()
assert sol.findMin( [3,4,5,1,2]) == 1
assert sol.findMin( [4,5,6,7,0,1,2]) == 0
assert sol.findMin( [11,13,15,17]) == 11
