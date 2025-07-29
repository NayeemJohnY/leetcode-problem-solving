# https://leetcode.com/problems/fibonacci-number/
class Solution:

    def fib_sol_1(self, n:int)-> int:
        if n <=1:
            return n
        return self.fib_sol_1(n-1) + self.fib_sol_1(n-2)
    
    def fib_sol_2(self, n:int, memo)-> int:
        if memo[n] is not None:
            return memo[n]
        if n <=1:
            result = n
        else:
            result = self.fib_sol_2(n-1, memo) + self.fib_sol_2(n-2, memo)
        memo[n] = result
        return result
    
    def fib_sol_3(self, n:int)-> int:
        if n <=1:
            return n
        dp = [None] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
    def fib(self, n: int) -> int:
        # Solution 1 - Recursive
        res1 = self.fib_sol_1(n)
        print("res1", res1)
      
        # Solution 2 - Memoization - reduce same calculations
        memo = [None] * (n+1)
        res2 = self.fib_sol_2(n, memo)
        print("res2", res2)
        
        res3 = self.fib_sol_3(n)
        print("res3", res3)
        assert res1 == res2 == res3

sol = Solution()
sol.fib(5)
