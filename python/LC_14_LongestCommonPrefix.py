# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        j = 0
        while j < len(prefix):
            is_mismatch_found = False
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != prefix[j]:
                    is_mismatch_found = True
                    break
            if is_mismatch_found:
                break
            j += 1
        return prefix[0:j]


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
print(sol.longestCommonPrefix(strs=["dog", "racecar", "car"]))
