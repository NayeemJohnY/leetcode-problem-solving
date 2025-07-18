// https://leetcode.com/problems/remove-element/description
public class LC_27_RemoveElement {

    public int removeElement(int[] nums, int val) {
        int index = 0;
        for (int num : nums) {
            if (num != val)
                nums[index++] = num;
        }
        return index;
    }
}