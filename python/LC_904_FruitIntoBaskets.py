# https://leetcode.com/problems/fruit-into-baskets/
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map = {}
        start, maxTotal = 0, 0
        for end in range(len(fruits)):
            map[fruits[end]] = map.get(fruits[end], 0)+1
            while len(map) > 2:
                map[fruits[start]] = map[fruits[start]] - 1
                if map[fruits[start]] == 0:
                    del map[fruits[start]]
                start += 1
            maxTotal = max(maxTotal, end-start+1)
        return maxTotal


sol = Solution()
print(sol.totalFruit([1, 2, 1]))
print(sol.totalFruit([0, 1, 2, 2]))
print(sol.totalFruit([1, 2, 3, 2, 2]))
print(sol.totalFruit([4, 1, 1, 1, 3, 1, 7, 5]))
