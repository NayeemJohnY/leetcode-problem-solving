// https://leetcode.com/problems/valid-parentheses/
import java.util.HashMap;
import java.util.Stack;


class LC_20_ValidParantheses {
    public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    // boolean valid = true;
    // for (Character ch : s.toCharArray()) {
    //     if (ch == '(' | ch == '{' || ch == '['){
    //         stack.add(ch);
    //     }
    //     else {
    //         if (stack.empty()){
    //             valid = false;
    //             break;
    //         }
    //         if (ch == ']' && stack.pop() != '['){
    //             valid = false;
    //             break;
    //         }
    //         if (ch == ')' && stack.pop() != '('){
    //             valid = false;
    //             break;
    //         }
    //         if (ch == '}' && stack.pop() != '{'){
    //             valid = false;
    //             break;
    //         }
    //     }
    // }
    // if (valid) {
    //     valid =  stack.empty();
    // }
    // return valid;
    // Using HashMap
    HashMap<Character, Character> map = new HashMap<Character, Character>(){{
        put(')', '(');
        put(']', '[');
        put('}', '{');
    }};
    for (Character ch : s.toCharArray()) {
        if (map.containsValue(ch)){
            stack.add(ch);
        }
        else if (stack.empty() || stack.pop() != map.get(ch)){
            return false;
        }
    }
    return stack.empty();
    }

}
        