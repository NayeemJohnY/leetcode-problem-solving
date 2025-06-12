class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # min_value = nums[0]
        # for i in range(1, len(nums)-1):
        #     if nums[i] < min_value:
        #         min_value = nums[i]
        # return min_value
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


solution = Solution()
print(solution.findMin([3, 4, 5, 1, 2]))
print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))

# [0, 1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7, 0]
# [2, 3, 4, 5, 6, 7, 0, 1]
# [3, 4, 5, 6, 7, 0, 1, 2]
# [4, 5, 6, 7, 0, 1, 2, 3]
# [5, 6, 7, 0, 1, 2, 3, 4]
# [6, 7, 0, 1, 2, 3, 4, 5]
# [7, 0, 1, 2, 3, 4, 5, 6]
# [0, 1, 2, 3, 4, 5, 6, 7]

# Elements gets their places when the rotation is 0 or multiple of len of elements (8)
# if not rotated or fully rotates = First a[0]
# if first rotation = last a[len(a)-1]
# half rotation element will be in middle len/2 rotation = a[len(a)//2]
# [0,1,2,4,5,6,7]

# [1,2,4,5,6,7,0]
# [2,4,5,6,7,0,1]

# [4,5,6,7,0,1,2]
# a[0] < a[mid]
# a[0] < a[len]
# a[len] < a[mid]
# a[mid] - a[len]

# [5,6,7,0,1,2,4]
# [6,7,0,1,2,4,5]
# [7,0,1,2,4,5,6]
# 0 > len
# 0 > mid
# mid < len

# [0,1,2,4,5,6,7]
