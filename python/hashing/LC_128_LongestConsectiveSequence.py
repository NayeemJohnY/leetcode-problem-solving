# https://leetcode.com/problems/longest-consecutive-sequence
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxLen = 0
        for num in nums_set:
            if num- 1 not in nums_set:
                current_num = num
                counter = 1
                while(current_num +1 in nums_set):
                    current_num += 1
                    counter += 1
                maxLen = max(maxLen, counter)
        return maxLen
    
sol = Solution()
assert sol.longestConsecutive([100,4,200,1,3,2]) == 4
assert sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
assert sol.longestConsecutive([1,0,1,2]) == 3
assert sol.longestConsecutive([0,0,-1]) == 2

                    
                