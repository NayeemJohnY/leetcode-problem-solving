package binary_search;
// https://leetcode.com/problems/first-bad-version

public class LC_278_FirstBadVersion {

    boolean isBadVersion(int version) {
        return true;
    }

    public int firstBadVersion(int n) {
        int left = 0, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
}