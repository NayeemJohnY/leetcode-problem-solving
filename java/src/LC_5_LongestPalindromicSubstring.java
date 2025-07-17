// https://leetcode.com/problems/longest-palindromic-substring

public class LC_5_LongestPalindromicSubstring {

    public int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    public void lenOfLongestPalindromicSubstring(String s) {
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {

            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }

        System.out.println(s.substring(start, end + 1));

    }

    public static void main(String[] args) {
        LC_5_LongestPalindromicSubstring solution = new LC_5_LongestPalindromicSubstring();
        solution.lenOfLongestPalindromicSubstring("babad");
        solution.lenOfLongestPalindromicSubstring("cbbd");
        solution.lenOfLongestPalindromicSubstring("madam");
    }
}