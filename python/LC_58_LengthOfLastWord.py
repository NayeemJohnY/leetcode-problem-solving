# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Solution 1
        words = [word for word in s.split() if word.strip != ""]
        # return len(words[-1])
    
        # Solution 2
        i = len(s)-1
        while i >=0 and s[i] == ' ':
            i-=1
        length = 0
        while i >= 0 and s[i] != ' ':
            i -=1
            length+= 1
        return length

    