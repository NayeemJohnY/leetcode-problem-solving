package sliding_window;

// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
public class LC_1343_NumberOfSubArraysAverageThreshold {
  public int numOfSubarrays(int[] arr, int k, int threshold) {
    int subArraysCount = 0, sum = 0, minSum = k * threshold;
    for (int i = 0; i < k; i++) {
      sum += arr[i];
    }
    if (sum >= minSum) {
      subArraysCount++;
    }

    for (int j = k; j < arr.length; j++) {
      sum += arr[j] - arr[j - k];
      if (sum > minSum) {
        subArraysCount++;
      }
    }
    return subArraysCount;
  }
}
