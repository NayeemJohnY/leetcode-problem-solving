package sliding_window;

// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters
import java.util.HashMap;
import java.util.HashSet;

public class LC_1876_SubstringsOfSizeThreeDistinctChars {

  public int countGoodSubstrings(String s) {
    int substringCount = 0, k = 3, left = 0;
    HashMap<Character, Integer> map = new HashMap<>();

    for (int j = 0; j < s.length(); j++) {
      map.put(s.charAt(j), map.getOrDefault(s.charAt(j), 0) + 1);

      if (j - left == k) {
        char ch = s.charAt(left);
        map.put(ch, map.get(ch) - 1);
        if (map.get(ch) == 0) {
          map.remove(ch);
        }
        left++;
      }

      if (map.size() == k) {
        substringCount++;
      }
    }
    return substringCount;
  }

  public int countGoodSubstrings_firstSol(String s) {
    int substringCount = 0, k = 3;
    HashMap<Character, Integer> map = new HashMap<>();
    for (int i = 0; i < k && i < s.length(); i++) {
      map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
    }
    if (map.size() == k) {
      substringCount++;
    }

    for (int j = k; j < s.length(); j++) {
      map.put(s.charAt(j - k), map.get(s.charAt(j - k)) - 1);
      if (map.get(s.charAt(j - k)) == 0) {
        map.remove(s.charAt(j - k));
      }
      map.put(s.charAt(j), map.getOrDefault(s.charAt(j), 0) + 1);
      if (map.size() == k) {
        substringCount++;
      }
    }
    return substringCount;
  }

  public int countGoodSubstrings_usingSet(String s) {
    int substringCount = 0, k = 3, left = 0;
    HashSet<Character> hashSet = new HashSet<>();
    for (int j = 0; j < s.length(); j++) {
      while (hashSet.contains(s.charAt(j))) {
        hashSet.remove(s.charAt(left++));
      }

      hashSet.add(s.charAt(j));

      if (hashSet.size() == k) {
        substringCount++;
        hashSet.remove(s.charAt(left++));
      }
    }
    return substringCount;
  }
}
