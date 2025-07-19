# https://leetcode.com/problems/reverse-words-in-a-string
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word for word in s.strip().split(" ")[::-1] if word.strip() != "")
    
    def reverseWords_sol_2(self, s: str) -> str:
        words = s.split()
        output = ""
        for i in range(len(words)-1, -1, -1):
            if words[i].strip() != "":
                output += words[i]
                if i != 0:
                    output += " "
        return output
    
sol = Solution()
sol.reverseWords_sol_2("a good   example")
                