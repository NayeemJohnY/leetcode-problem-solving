class Solution(object):
    def containsDuplicate(self, nums: list):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1
        # for i in range(0, len(nums)):
        #     if nums[i] in nums[:i] or nums[i] in nums[i+1:]:
        #         return True
        # return False

        # Solution 2
        # for i in range(0, len(nums)):
        #     if nums[i] in nums[i+1:]:
        #         return True
        # return False

        # Solution 3
        return len(set(nums)) != len(nums)

        # Solution 4 - Legacy:
        # n =len(nums)
        # for i in range(0, n-1):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Solution 5
        # nums.sort()
        # for i in range(0, len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
