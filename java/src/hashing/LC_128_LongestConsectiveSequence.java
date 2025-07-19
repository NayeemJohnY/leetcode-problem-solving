package hashing;

// https://leetcode.com/problems/longest-consecutive-sequence
import java.util.HashSet;

public class LC_128_LongestConsectiveSequence {

    public void lengthOfLongestConsectiveSequence(int[] arr) {

        HashSet<Integer> sequence = new HashSet<>();
        for (int num : arr) {
            sequence.add(num);
        }

        int longestSeqCount = 0, count = 0, currentNum = 0;
        for (Integer num : sequence) {
            if (!sequence.contains(num - 1)) {
                currentNum = num;
                count = 1;

                while (sequence.contains(currentNum + 1)) {
                    currentNum++;
                    count++;
                }

                if (count > longestSeqCount) {
                    longestSeqCount = count;
                }
            }
        }
        System.out.println(longestSeqCount);

    }

    public static void main(String[] args) {
        LC_128_LongestConsectiveSequence sol = new LC_128_LongestConsectiveSequence();
        sol.lengthOfLongestConsectiveSequence(new int[] { 100, 4, 200, 1, 3, 2 });
        sol.lengthOfLongestConsectiveSequence(new int[] { 0, 3, 7, 2, 5, 8, 4, 6, 0, 1 });
        sol.lengthOfLongestConsectiveSequence(new int[] { 1, 0, 1, 2 });
    }
}
