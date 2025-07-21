# https://leetcode.com/problems/delete-characters-to-make-fancy-string

class Solution:
    def makeFancyString(self, s: str) -> str:
        counter = 1
        output = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                counter = 1
            else:
                counter += 1
            if counter < 3:
                output.append(s[i])

        return "".join(output)
