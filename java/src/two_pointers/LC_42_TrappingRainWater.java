package two_pointers;
// https://leetcode.com/problems/trapping-rain-water
import java.util.Arrays;

public class LC_42_TrappingRainWater {
    public int trapSol1(int[] height) {
        int n = height.length;
        int[] leftMax = new int[n];
        int[] rightMax = new int[n];
        leftMax[0] = height[0];
        rightMax[n - 1] = height[n - 1];
        for (int i = 1; i < n; i++) {
            if (height[i] < leftMax[i - 1])
                leftMax[i] = leftMax[i - 1];
            else
                leftMax[i] = height[i];

        }
        System.out.println("Left Max: " + Arrays.toString(leftMax));
        for (int i = n - 2; i >= 0; i--) {
            if (height[i] < rightMax[i + 1])
                rightMax[i] = rightMax[i + 1];
            else
                rightMax[i] = height[i];
        }
        System.out.println("Right Max: " + Arrays.toString(rightMax));

        int totalTrap = 0;
        for (int j = 0; j < n; j++)
            totalTrap += Math.min(leftMax[j], rightMax[j]) - height[j];
        return totalTrap;
    }

    public int trapSol2(int[] height) {
        int n = height.length;
        int[] leftMax = new int[n];
        int[] rightMax = new int[n];
        leftMax[0] = height[0];
        rightMax[n - 1] = height[n - 1];
        for (int i = 1; i < n; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], height[i]);
        }
        System.out.println("Left Max: " + Arrays.toString(leftMax));

        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], height[i]);
        }
        System.out.println("Right Max: " + Arrays.toString(rightMax));

        int totalTrap = 0;
        for (int j = 0; j < n; j++) {
            totalTrap += Math.min(leftMax[j], rightMax[j]) - height[j];
        }
        return totalTrap;
    }

    public int trapSol3(int[] height) {
        int left = 0, right = height.length -1, leftMax=0, rightMax=0, totalTrap = 0;
        while(left < right){

            if (height[left]< height[right]){
                if (height[left]> leftMax)
                    leftMax = height[left];
                else
                    totalTrap += leftMax - height[left];
                left++;
            }
            else {
                if (height[right] > rightMax)
                    rightMax = height[right];
                else
                    totalTrap += rightMax - height[right];
                right--;
            }
        }
        return totalTrap;
    }

    public int trapSol4(int[] height) {
        int left = 0, right = height.length -1;
        int leftMax=height[left], rightMax=height[right], totalTrap = 0;
        while(left < right){
            if (leftMax < rightMax){
                left++;
                if (height[left]> leftMax)
                    leftMax = height[left];
                else
                    totalTrap += leftMax - height[left];
            }
            else {
                right--;
                if (height[right] > rightMax)
                    rightMax = height[right];
                else
                    totalTrap += rightMax - height[right];
            }
        }
        return totalTrap;
    }

    public int trapSol5(int[] height) {
        int left = 0, right = height.length -1;
        int leftMax=height[left], rightMax=height[right], totalTrap = 0;
        while(left < right){
            if (leftMax < rightMax){
                left++;
                leftMax = Math.max(leftMax, height[left]);
                totalTrap += leftMax - height[left];
            }
            else {
                right--;
                rightMax = Math.max(rightMax, height[right]);
                totalTrap += rightMax - height[right];
            }
        }
        return totalTrap;
    }

    public static void main(String[] args) {
        LC_42_TrappingRainWater trappingRainWater = new LC_42_TrappingRainWater();
        System.out.println(
                "Total Water Sol 1: " + trappingRainWater.trapSol1(new int[] { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 }));
        System.out.println(
                "Total Water Sol 3: " + trappingRainWater.trapSol3(new int[] { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 }));
        System.out.println("Total Water Sol 2: " + trappingRainWater.trapSol2(new int[] { 4, 2, 0, 3, 2, 5 }));
        System.out.println("Total Water Sol 3: " + trappingRainWater.trapSol3(new int[] { 4, 2, 0, 3, 2, 5 }));
        System.out.println("Total Water Sol 4: " + trappingRainWater.trapSol4(new int[] { 4, 2, 0, 3, 2, 5 }));
        System.out.println("Total Water Sol 5: " + trappingRainWater.trapSol5(new int[] { 4, 2, 0, 3, 2, 5 }));
        System.out.println("Total Water Sol 5: " + trappingRainWater.trapSol5(new int[] { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 }));
    }
}
