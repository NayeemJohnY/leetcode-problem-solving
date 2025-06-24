
import java.util.HashSet;

public class Solution_ContainsDuplicate {
    
    public boolean containsDuplicate(int[] nums) {
        // Solution 1
        // for (int i = 0; i < nums.length -1; i++){
        //     for (int j = i +1; j < nums.length; j++){
        //         if (nums[i] == nums[j]){
        //             return true;
        //         }
        //     }
        // }
        // return false;

        // Solution 2
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++){
            System.out.println(set);
            if (set.contains(nums[i])){
                return true;
            }
            set.add(nums[i]);
        }
        return false;


    }


    public static void main(String[] args) {
        Solution_ContainsDuplicate solution = new Solution_ContainsDuplicate();
        System.out.println("Hello");
        System.out.println(solution.containsDuplicate(new int[]{1, 2, 3, 1}));
        System.out.println(solution.containsDuplicate(new int[]{1, 2, 3, 4}));
        System.out.println(solution.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}));
    }
}
