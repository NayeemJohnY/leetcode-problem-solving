package hashing;

import java.util.HashSet;

public class LC_3487_MaximumUniqueSubarraySumAfterDeletion {

    public int maxSum(int[] nums) {
        HashSet<Integer> unique = new HashSet<>();
        int maxSum = 0, maxEle = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num >= 0 && !unique.contains(num)) {
                unique.add(num);
                maxSum += num;
            } else if (num < 0 && unique.isEmpty()) {
                maxEle = Math.max(maxEle, num);
            }
        }
        return unique.isEmpty() ? maxEle : maxSum;
    }
}
