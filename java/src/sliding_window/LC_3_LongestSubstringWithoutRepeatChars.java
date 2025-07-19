package sliding_window;
//  https://leetcode.com/problems/longest-substring-without-repeating-characters

import java.util.HashSet;

public class LC_3_LongestSubstringWithoutRepeatChars {

       public void lengthOfLongestSubstring(String s) {
        int left = 0, right = 0, maxLength = 0;
        HashSet<Character> charactersSet = new HashSet<>();
        while (right < s.length()) {
            char currentChar = s.charAt(right);
            if (!charactersSet.contains(currentChar)) {
                charactersSet.add(currentChar);
                maxLength = Math.max(maxLength, right - left + 1);
                right++;
            } else {
                charactersSet.remove(s.charAt(left));
                left++;
            }
        }
        System.out.println(maxLength);
    }

    public static void main(String[] args) {
        LC_3_LongestSubstringWithoutRepeatChars solution = new LC_3_LongestSubstringWithoutRepeatChars();
        solution.lengthOfLongestSubstring("abcabcbb");
        solution.lengthOfLongestSubstring("bbbbbb");
        solution.lengthOfLongestSubstring("pwwkew");
    }
}
