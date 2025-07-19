package sliding_window;

import java.util.HashMap;

// https://leetcode.com/problems/fruit-into-baskets/
public class LC_904_FruitIntoBaskets {
    public int totalFruit(int[] fruits) {
        HashMap<Integer, Integer> fruitMap = new HashMap<>();
        int start = 0, maxTotal = 0;
        for (int end = 0; end < fruits.length; end++) {
            fruitMap.put(fruits[end], fruitMap.getOrDefault(fruits[end], 0) + 1);
            while (fruitMap.size() > 2) {
                int f = fruits[start++];
                fruitMap.put(f, fruitMap.get(f) - 1);
                if (fruitMap.get(f) == 0)
                    fruitMap.remove(f);
            }
            maxTotal = Math.max(maxTotal, end - start + 1);
        }
        return maxTotal;
    }
}
