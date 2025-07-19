package two_pointers;

public class LC_11_ContainerWithMostWater {

    public int maxArea(int[] height) {
        int left =0, right = height.length-1;
        int areaMax = 0;
        while (left < right){
            int area = (right - left) * height[height[left] < height[right] ? left++ : right--];
            if (area > areaMax)
                areaMax = area;
        }
        return areaMax;
    }
}
