# https: // leetcode.com/problems/first-bad-version

def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            is_bad = isBadVersion(mid)
            if is_bad:
                right = mid
            else:
                left = mid + 1

        return left
