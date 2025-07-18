// https://leetcode.com/problems/longest-common-prefix/

public class LC_14_LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        int i;
        for (i = 0; i < strs[0].length(); i++) {
            char ch = strs[0].charAt(i);
            boolean isMisMatchFound = false;
            for (int j = 1; j < strs.length; j++) {
                String str = strs[j];
                if (i >= str.length() || str.charAt(i) != ch) {
                    isMisMatchFound = true;
                    break;
                }
            }
            if (isMisMatchFound)
                break;
        }
        return strs[0].substring(0, i);
    }
}
