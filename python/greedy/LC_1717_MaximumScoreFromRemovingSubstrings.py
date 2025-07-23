# https://leetcode.com/problems/maximum-score-from-removing-substrings
class Solution:
    
    def calcuateGain(self, stack, s, substr):
        count = 0
        print(stack, s, substr)
        for c in s:
            if c == substr[1] and stack and stack[-1] == substr[0]:
                count += 1
                stack.pop()
            else:
                stack.append(c)
        return count
    
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        substr1, substr2 = "ab", "ba"
        if y > x:
            substr2, substr1 = "ab", "ba"
            x, y = y, x

        max_points = 0
        max_points = self.calcuateGain(stack, s, substr1) * x
        remaining = "".join(stack)
        stack.clear()
        max_points = max_points + self.calcuateGain(stack, remaining, substr2) * y
        return max_points
    
sol = Solution()
sol.maximumGain(s = "aabbaaxybbaabb", x = 5, y = 4)


        