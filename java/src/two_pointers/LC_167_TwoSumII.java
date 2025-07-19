package two_pointers;
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

public class LC_167_TwoSumII {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target)
                return new int[] { left + 1, right + 1 };
            if (sum > target)
                right--;
            else
                left++;
        }
        return new int[] { -1, -1 };
    }
}