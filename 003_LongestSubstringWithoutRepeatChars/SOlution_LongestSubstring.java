import java.util.HashSet;

public class SOlution_LongestSubstring {
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
        SOlution_LongestSubstring solution = new SOlution_LongestSubstring();
        solution.lengthOfLongestSubstring("abcabcbb");
        solution.lengthOfLongestSubstring("bbbbbb");
        solution.lengthOfLongestSubstring("pwwkew");
    }
}
