
public class Solution_SumOfTwoIntegers {

    public void bitwiseSum(int a, int b) {
        int sum = 0;
        while (b != 0) {
            sum = a ^ b;
            b = (a & b) << 1;
            a = sum;
        }
        System.out.println(a);
    }

    public static void main(String[] args) {
        Solution_SumOfTwoIntegers solution = new Solution_SumOfTwoIntegers();
        solution.bitwiseSum(10, 29);
        solution.bitwiseSum(-21, 2);
        solution.bitwiseSum(5, -7);
        solution.bitwiseSum(15, -5);
        solution.bitwiseSum(-5, -6);

    }
}