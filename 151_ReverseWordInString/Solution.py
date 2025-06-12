
class Solution(object):
    def reverseWords(self, s: str):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        output = ''
        for i in range(len(words)-1, -1, -1):
            output += words[i]
            if i != 0:
                output += " "
        return output

        # Solution 2
        # return ' '.join(s.strip().split()[::-1])


solution = Solution()
print(solution.reverseWords("the sky is blue"))
print(solution.reverseWords("  hello world  "))
print(solution.reverseWords("a good   example"))
