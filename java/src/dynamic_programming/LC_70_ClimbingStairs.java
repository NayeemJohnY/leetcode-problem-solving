package dynamic_programming;
// https://leetcode.com/problems/climbing-stairs/

public class LC_70_ClimbingStairs {

    public int climbStairs(int n) {
        if (n <= 1)
            return n;
        int[] dp = new int[n + 1];
        dp[0] = dp[1] = 1;
        for (int i = 0; i < n + 1; i++)
            dp[i] = dp[i - 1] + dp[i - 2];
        return dp[n];
    }
}
