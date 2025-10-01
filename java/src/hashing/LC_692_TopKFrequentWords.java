package hashing;

import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;

public class LC_692_TopKFrequentWords {

    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String, Integer> freqMap = new HashMap<>();
        for (String word : words) {
            freqMap.put(word, freqMap.getOrDefault(word, 0)+ 1);
        }

        Comparator<String> comparator = ((a, b) -> {
            int freqCompare = freqMap.get(a).compareTo(freqMap.get(b));
            if (freqCompare == 0) {
                return a.compareTo(b);
            }
            return freqCompare;
        });
        comparator = comparator.thenComparing(Comparator.naturalOrder());
        PriorityQueue<String> queue = new PriorityQueue<>(comparator);

        for (String word : freqMap.keySet()) {
            queue.add(word);
            if (queue.size() > k)
                queue.poll();
        }

        return queue.stream().limit(k).toList();
    }
}
