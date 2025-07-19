# https://leetcode.com/problems/find-smallest-letter-greater-than-target
from typing import List
#  

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left , right = 0, len(letters)-1
        while left <= right:
            mid = left + (right - left) // 2 
            if target >= letters[mid]:
                left = mid + 1
            else:
                right = mid -1
        return letters[left % len(letters)]
    
sol = Solution()
print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "c"))