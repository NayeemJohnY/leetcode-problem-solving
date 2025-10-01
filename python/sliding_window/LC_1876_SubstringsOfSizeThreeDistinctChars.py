# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        substring_count = left = 0
        k = 3
        map = {}
        for right in range(len(s)):
            map[s[right]] = map.get(s[right], 0) + 1
            if right - left == k:
                ch = s[left]
                map[ch] -= 1
                if map[ch] == 0:
                    del map[ch]
            if len(map) == k:
                substring_count += 1
        return substring_count

    def countGoodSubstrings_using_set(self, s: str) -> int:
        substring_count = left = 0
        k = 3
        window = set()
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            if len(window) == k:
                substring_count += 1
                window.remove(s[left])
                left += 1
        return substring_count
