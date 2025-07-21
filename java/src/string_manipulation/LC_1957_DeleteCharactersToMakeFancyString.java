package string_manipulation;
// https://leetcode.com/problems/delete-characters-to-make-fancy-string

public class LC_1957_DeleteCharactersToMakeFancyString {
    public String makeFancyString(String s) {
        char[] ch = s.toCharArray();
        int counter = 1, index = 1;
        for (int i = 1; i < ch.length; i++) {
            if (ch[i] != ch[i - 1]) {
                counter = 1;
            } else {
                counter += 1;
            }
            if (counter > 2)
                ch[index++] = ch[i];
        }

        return new String(ch, 0, index);
    }
}
