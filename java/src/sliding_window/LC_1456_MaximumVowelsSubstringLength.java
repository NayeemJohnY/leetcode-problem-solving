package sliding_window;
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length


public class LC_1456_MaximumVowelsSubstringLength {

  public int isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ? 1 : 0;
  }

  public int maxVowels(String s, int k) {
    int vowelsMax = 0, vowelsCount = 0;

    for (int i = 0; i < k; i++) {
      vowelsCount += isVowel(s.charAt(i));
    }
    vowelsMax = vowelsCount;
    for (int j = k; j < s.length(); j++) {
      vowelsCount -= isVowel(s.charAt(j - k));
      vowelsCount += isVowel(s.charAt(j));
      vowelsMax = Math.max(vowelsMax, vowelsCount);
    }

    return vowelsMax;
  }
}
