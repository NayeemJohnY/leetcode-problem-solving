# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(c):
            return 1 if c in "aeiou" else 0
        vowel_count = 0
        for ch in s[:k]:
            vowel_count += isVowel(ch)
        max_vowel = vowel_count
        for i in range(k, len(s)):
            vowel_count -= isVowel(s[i-k]) 
            vowel_count += isVowel(s[i])
            max_vowel = max(max_vowel, vowel_count)
        return max_vowel