package greedy;
// https://leetcode.com/problems/maximum-score-from-removing-substrings
public class LC_1717_MaximumScoreFromRemovingSubstrings {

    public int[] calculateGain(char[] chars, int length, String substr) {
        int counter = 0;
        int i = 0;
        for (int j = 0; j < length; j++) {
            char ch = chars[j];
            if (i > 0 && ch == substr.charAt(1) && chars[i - 1] == substr.charAt(0)) {
                counter++;
                i--;
            } else {
                chars[i++] = ch;
            }
        }
        return new int[] { counter, i };
    }

    public int maximumGain(String s, int x, int y) {
        int maxPoints = 0;
        String subStr1 = "ab", subStr2 = "ba";
        int score1 = x, score2 = y;
        if (y > x) {
            subStr1 = "ba";
            subStr2 = "ab";
            score1 = y;
            score2 = x;
        }
        char[] chars = s.toCharArray();

        int[] output = calculateGain(chars, chars.length, subStr1);
        maxPoints += output[0] * score1;

        output = calculateGain(chars, output[1], subStr2);
        maxPoints += output[0] * score2;

        return maxPoints;

    }

    public static void main(String[] args) {
        LC_1717_MaximumScoreFromRemovingSubstrings removingSubstrings = new LC_1717_MaximumScoreFromRemovingSubstrings();
        System.out.println(removingSubstrings.maximumGain("cdbcbbaaabab", 4, 5));
        System.out.println(removingSubstrings.maximumGain("aabbaaxybbaabb", 5, 4));
    }
}
