class Solution:
    def rec(self, n, dp):
        
        if n == 0 or n == 1:
            return n
        if dp[n] != -1:
            return dp[n]
        # recursive case
        dp[n] = self.rec(n-1,dp) + self.rec(n - 2,dp)
        return dp[n]

    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.rec(n,dp)

        # Using Iteration
        """
        first = 0
        second = 1
        for i in range(n):
            third = first + second

            first = second
            second = third
        return first
        """
        # Using Recursion
        """
        # base case
        if  n == 0 or n == 1:
            return n
        
        # recursive case
        return self.fib(n-1) + self.fib(n-2)
        """