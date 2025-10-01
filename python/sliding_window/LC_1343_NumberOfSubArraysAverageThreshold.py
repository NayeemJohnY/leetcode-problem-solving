# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        for num in arr[:k]:
            total += num
        arr_count = 0
        if total // k >= threshold:
            arr_count += 1
        
        for i in range(k, len(arr)):
            total -= arr[i-k]
            total += arr[i]
            if total // k >= threshold:
                arr_count += 1
        return arr_count
    
    def numOfSubarrays_2(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        min_sum = k * threshold
        for num in arr[:k]:
            total += num
        arr_count = 0
        if total >= min_sum:
            arr_count += 1
        
        for i in range(k, len(arr)):
            total += arr[i] - arr[i-k]
            if total >= min_sum:
                arr_count += 1
        return arr_count

