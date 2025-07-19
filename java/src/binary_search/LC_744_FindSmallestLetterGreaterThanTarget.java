package binary_search;
// https://leetcode.com/problems/find-smallest-letter-greater-than-target

public class LC_744_FindSmallestLetterGreaterThanTarget {

    public char nextGreatestLetter(char[] letters, char target) {
        int left = 0, right = letters.length;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target >= letters[mid])
                left = mid + 1;
            else
                right = mid - 1;
        }
        return letters[left % letters.length];
    }

    public static void main(String[] args) {
        LC_744_FindSmallestLetterGreaterThanTarget greaterThanTarget = new LC_744_FindSmallestLetterGreaterThanTarget();
        System.out.println(greaterThanTarget.nextGreatestLetter(new char[]{'c', 'f', 'g'}, 'a'));
    }
}