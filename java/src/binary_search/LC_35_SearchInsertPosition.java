package binary_search;
// https://leetcode.com/problems/search-insert-position

public class LC_35_SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target)
                return mid;
            if (nums[mid] > target)
                right = mid;
            else
                left = mid + 1;
        }
        return left + (nums[left] < target ? 1 : 0);
    }
}