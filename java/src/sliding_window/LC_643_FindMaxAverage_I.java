package sliding_window;
// https://leetcode.com/problems/maximum-average-subarray-i/
public class LC_643_FindMaxAverage_I {

    public double findMaxAverage(int[] nums, int k) {
        int currentSum = 0, maxSum = 0;
        for (int i = 0; i < k; i++)
            currentSum += nums[i];
        maxSum = currentSum;
        for (int j = k; j < nums.length; j++) {
            currentSum += nums[j] - nums[j - k];
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum / (double) k;
    }
}
