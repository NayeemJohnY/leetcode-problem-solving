package stack;
// https://leetcode.com/problems/removing-stars-from-a-string

import java.util.Stack;

public class LC_2390_RemovingStarsFromAString {

    public String removeStars(String s) {
        // Solution 1
        char[] arr = s.toCharArray();
        int i = 0;
        for (char ch : arr) {
            if (ch == '*')
                i--;
            else
                arr[i++] = ch;
        }
        s = new String(arr, 0, i);
        // Solution 2
        Stack<Character> charStack = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch == '*')
                charStack.pop();
            else
                charStack.push(ch);
        }
        StringBuilder stringBuilder = new StringBuilder();
        for (char ch : charStack)
            stringBuilder.append(ch);
        s = stringBuilder.toString();

        return s;
    }
}
