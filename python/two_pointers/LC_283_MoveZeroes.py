# https://leetcode.com/problems/move-zeroes/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        while index <len(nums):
            nums[index] = 0
            index += 1

sol = Solution()
nums  = [1,2, 0, 4, 0, 0, 6, 0, 9]
sol.moveZeroes(nums)
print(nums)