package bit_manipulation;

// https://leetcode.com/problems/single-number/

public class LC_136_SingleNumber {

    public int singleNumber(int[] nums) {
        int singleNum = 0;
        for (int num : nums) {
            singleNum ^= num;
        }
        return singleNum;
    }
}
