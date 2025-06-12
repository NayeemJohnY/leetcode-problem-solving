class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0 (n^2) Solution - Brute Force Solution
        seq = set()
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j] and nums[i]-nums[j] == 1:
                    seq.update([nums[j], nums[i]])
                elif nums[i] < nums[j] and nums[j] - nums[i] == 1:
                    seq.update([nums[i], nums[j]])
        print('seq', seq)
        return len(seq)


sol = Solution()
sol.longestConsecutive([100, 4, 200, 1, 3, 2])
sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
sol.longestConsecutive([1, 0, 1, 2])