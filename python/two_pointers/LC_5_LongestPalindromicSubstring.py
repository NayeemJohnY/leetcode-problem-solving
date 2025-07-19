# https://leetcode.com/problems/longest-palindromic-substring
class Solution:

    def expand_around_center(self, s, left, right):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right-left-1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0., 0
        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i+1)
            sp_len = max(len1, len2)
            if sp_len > end-start:
                start = i - (sp_len-1)//2
                end = i + sp_len//2
        print(s[start:end+1])
        return s[start:end+1]


sol = Solution()
assert sol.longestPalindrome("babad") == "aba"
