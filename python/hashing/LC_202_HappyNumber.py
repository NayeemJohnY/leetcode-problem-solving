# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            digits_sum = 0
            while n > 0:
                digits_sum += (n % 10) ** 2
                n = n / 10
            n = digits_sum
        return True if n == 1 else False
