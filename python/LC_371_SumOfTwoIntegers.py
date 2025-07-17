# https://leetcode.com/problems/sum-of-two-integers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFF
        MAX_INT = 2**31 -1
        while b != 0:
            sum  = (a ^ b) & MASK
            b =  ((a & b) << 1) & MASK
            a = sum
        return a if a <= MAX_INT else ~(a ^ MASK)
    
sol = Solution()
assert sol.getSum(5, 3) == 8
assert sol.getSum(1, 2) == 3
assert sol.getSum(2, 3) == 5

