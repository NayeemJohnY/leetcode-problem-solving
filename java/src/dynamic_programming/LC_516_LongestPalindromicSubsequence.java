package dynamic_programming;
// https://leetcode.com/problems/longest-palindromic-subsequence/
public class LC_516_LongestPalindromicSubsequence {

    public static int longestPalindromeSubseq(String s) {
        int[][] dp = new int[s.length()][s.length()];
        for (int i = s.length() - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i + 1; j < s.length(); j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = 2 + dp[i + 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][s.length() - 1];

    }

    public static void main(String[] args) {
        System.out.println(longestPalindromeSubseq("bbbab")); // Output: 4
        System.out.println(longestPalindromeSubseq("cbbd")); // Output: 2
        System.out.println(longestPalindromeSubseq("abcd")); // Output: 1
        System.out.println(longestPalindromeSubseq("madam"));
    }

}
