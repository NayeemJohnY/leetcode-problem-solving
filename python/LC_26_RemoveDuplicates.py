# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
    
sol = Solution()
nums = [1,1, 2, 3, 4, 5, 6, 6]
sol.removeDuplicates(nums)
print(nums)

nums = [1, 2, 3, 4, 5, 6, 7]
sol.removeDuplicates(nums)
print(nums)