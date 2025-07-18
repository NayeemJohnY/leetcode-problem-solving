
import java.util.Arrays;

// https://leetcode.com/problems/move-zeroes/
public class LC_283_MoveZeroes {
    public void moveZeroes(int[] nums) {
        int index = 0;
        for (int num : nums) {
            if (num != 0)
                nums[index++] = num;
        }

        for (int i = index; i < nums.length; i++) {
            nums[i] = 0;
        }
    }

    public static void main(String[] args) {
        LC_283_MoveZeroes moveZeroes = new LC_283_MoveZeroes();
        int[] nums = { 1, 2, 0, 4, 0, 0, 6, 7, 0 };
        moveZeroes.moveZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }

}
