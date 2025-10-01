# https://leetcode.com/problems/top-k-frequent-elements
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        res = sorted(freq_map, key=lambda x: freq_map[x], reverse=True)
        return res[:k]
