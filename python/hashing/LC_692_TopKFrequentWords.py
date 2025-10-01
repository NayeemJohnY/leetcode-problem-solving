# https://leetcode.com/problems/top-k-frequent-words
from typing import List
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_map = {}
        for word in words:
            freq_map[word] = freq_map.get(word, 0) + 1
        # res = sorted(freq_map, key=lambda x:freq_map[x], reverse=True)
        # print(res)
        # return res[:k]
        
        heap = []
        for word, freq in freq_map.items():
            heapq.heappush(heap, (-freq, word))
        return [heapq.heappop(heap)[1] for _ in range(k)]