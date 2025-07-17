# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")": "(", "}":"{", "]": "["}
        for c in s:
            if c in map.values():
                stack.append(c)
            elif not stack or stack.pop() != map.get(c):
                return False
        return not stack

sol = Solution()
assert sol.isValid("()") == True
assert sol.isValid("()[]{}") == True
assert sol.isValid("(]") == False
assert sol.isValid("([])") == True

        