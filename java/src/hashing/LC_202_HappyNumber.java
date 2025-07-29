package hashing;
// https://leetcode.com/problems/happy-number/

import java.util.HashSet;

public class LC_202_HappyNumber {

    public boolean isHappy(int n) {
        HashSet<Integer> seen = new HashSet<>();
        while (n != 1 && !seen.contains(n)) {
            int digitsSum = 0;
            while (n > 0) {
                digitsSum += Math.pow(n % 10, 2);
                n = n / 10;
            }
            n = digitsSum;
        }
        return n == 1 ? true : false;
    }
}
