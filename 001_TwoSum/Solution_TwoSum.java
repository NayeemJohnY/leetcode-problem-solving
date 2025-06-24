import java.util.HashMap;

public class Solution_TwoSum {
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
        Solution_TwoSum solution = new Solution_TwoSum();
        int[] indexes = solution.towSumHashMap(new int[] { 1, 2, 4, 5, 7, 8 }, 5);
        System.out.println(indexes[0] + " " + indexes[1]);
    }

}

// class Solution {
// public int firstUniqChar(String s) {
// HashMap<Character, Integer> map = new HashMap<>();
// for (int i=0; i<s.length(); i++){
// char charc = s.charAt(i);
// if (map.containsKey(charc)){
// map.put(charc, map.get(charc) + 1);
// }
// else {
// map.put(charc, 1);
// }
// }
// System.out.println(map);
// for (Map.Entry<Character, Integer> e : map.entrySet()){
// if (e.getValue() == 1){
// return s.indexOf(e.getKey());
// }
// }
// return -1;

// }
// }