
import java.util.Arrays;

// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

public class LC_26_RemoveDuplicates {
    public int removeDuplicates(int[] nums) {
        int index = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[index++] = nums[i];
            }
        }
        return index;
    }

    public static void main(String[] args) {
        LC_26_RemoveDuplicates duplicates = new LC_26_RemoveDuplicates();
        int[] nums = { 1, 1, 2, 3, 3, 4, 5, 6, 6 };
        int index = duplicates.removeDuplicates(nums);
        System.out.println(Arrays.toString(Arrays.copyOf(nums, index)));
    }
}