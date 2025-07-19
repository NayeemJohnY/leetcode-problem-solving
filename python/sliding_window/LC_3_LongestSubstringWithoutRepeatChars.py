# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_set = set()
        left, right, maxLen, best_start = 0, 0, 0, 0
        while right < len(s):
            if s[right] not in chars_set:
                chars_set.add(s[right])
                if right - left + 1 > maxLen:
                    maxLen = right - left + 1
                    best_start = left
                right += 1
            else:
                chars_set.remove(s[left])
                left += 1
        print(s[best_start : best_start+maxLen])
        return maxLen

sol = Solution()
assert sol.lengthOfLongestSubstring("abcabcbb") == 3
assert sol.lengthOfLongestSubstring("bbbbb") == 1
assert sol.lengthOfLongestSubstring("pwwkew") == 3