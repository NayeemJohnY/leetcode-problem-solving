package sliding_window;
// https://leetcode.com/problems/maximum-erasure-value

import java.util.HashSet;

public class LC_1695_MaximumErasureValue {
    public int maximumUniqueSubarray(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int left = 0, max_sum = 0, current_sum = 0;
        for (int num : nums) {
            while (set.contains(num)) {
                set.remove(nums[left]);
                current_sum -= nums[left];
                left++;
            }
            set.add(num);
            current_sum += num;
            max_sum = Math.max(max_sum, current_sum);
        }
        return max_sum;
    }
}
