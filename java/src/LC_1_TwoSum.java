// https://leetcode.com/problems/two-sum/description/
import java.util.HashMap;

public class LC_1_TwoSum {
    public int[] twoSum(int[] nums, int target) {
        for (int index = 0; index < nums.length; index++) {
            for (int j = index + 1; j < nums.length; j++) {
                if (nums[j] == target - nums[index]) {
                    return new int[] { index, j };
                }
            }
        }
        return new int[] {};
    }

    public int[] towSumHashMap(int[] nums, int target) {
        HashMap<Integer, Integer> numIndex = new HashMap<>();
        for (int index = 0; index < nums.length; index++) {
            if (numIndex.containsKey(target - nums[index])) {
                return new int[] { index, numIndex.get(target - nums[index]) };
            }
            numIndex.put(nums[index], index);
        }
        return new int[] {};
    }

    public static void main(String[] args) {
        LC_1_TwoSum solution = new LC_1_TwoSum();
        int[] indexes = solution.towSumHashMap(new int[] { 1, 2, 4, 5, 7, 8 }, 5);
        System.out.println(indexes[0] + " " + indexes[1]);
    }

}