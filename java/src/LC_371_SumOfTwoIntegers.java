// https://leetcode.com/problems/sum-of-two-integers

public class LC_371_SumOfTwoIntegers {

    public void bitwiseSum(int a, int b) {
        while (b != 0) {
            int sum = a ^ b;
            b = (a & b) << 1;
            a = sum;
        }
        System.out.println(a);
    }

    public static void main(String[] args) {
        LC_371_SumOfTwoIntegers solution = new LC_371_SumOfTwoIntegers();
        solution.bitwiseSum(10, 29);
        solution.bitwiseSum(-21, 2);
        solution.bitwiseSum(5, -7);
        solution.bitwiseSum(15, -5);
        solution.bitwiseSum(-5, -6);

    }
}
