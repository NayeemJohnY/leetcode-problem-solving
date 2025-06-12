class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in nums and nums.index(diff) != index:
                diff_index = nums.index(diff)
                return [index, diff_index]


solution = Solution()
print(solution.twoSum([1, 2, 4, 5, 7, 8], 15))
