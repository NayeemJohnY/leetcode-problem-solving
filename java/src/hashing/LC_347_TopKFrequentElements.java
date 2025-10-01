package hashing;

// https://leetcode.com/problems/top-k-frequent-elements

import java.util.Comparator;
import java.util.HashMap;
import java.util.PriorityQueue;


public class LC_347_TopKFrequentElements {

  public int[] topKFrequent(int[] nums, int k) {
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int num : nums) {
      map.put(num, map.getOrDefault(num, 0) + 1);
    }

    Comparator<Integer> comparator = (a, b) -> map.get(b) - map.get(a);

    return map.keySet().stream().sorted(comparator).limit(k).mapToInt(i -> i).toArray();
  }

  public int[] topKFrequentSolPriorityQueue(int[] nums, int k) {
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int num : nums) {
      map.put(num, map.getOrDefault(num, 0) + 1);
    }

    Comparator<Integer> comparator = (a, b) -> map.get(a) - map.get(b);
    PriorityQueue<Integer> queue = new PriorityQueue<>(comparator);

    for (int num : map.keySet()) {
      queue.add(num);
      if (queue.size() > k) {
        queue.poll();
      }
    }

    int[] res = new int[k];
    for (int i = 0; i < k; i++) {
      res[i] = queue.poll();
    }

    return res;
  }
}
