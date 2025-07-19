package string_manipulation;
// https://leetcode.com/problems/length-of-last-word

import java.util.Arrays;

public  class LC_58_LengthOfLastWord {
    
    public int lengthOfLastWord(String s) {
        // Solution 1
        String[] words = s.trim().split("\\s+");
        System.out.println(Arrays.toString(words));
        // return words[words.length-1].length();

        // Solution 2
        int i = s.length()-1;
        while(i >=0 && s.charAt(i) == ' ')
            i--;
        int length = 0;
        while(i >=0 && s.charAt(i) != ' '){
            i--;
            length++;
        }
        return length;
    }

    public static void main(String[] args) {
        LC_58_LengthOfLastWord lastWord = new LC_58_LengthOfLastWord();
        System.out.println(lastWord.lengthOfLastWord("   fly me   to   the moon  "));
    }
}