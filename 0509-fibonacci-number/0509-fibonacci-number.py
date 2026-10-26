class Solution:
    def fib(self, n: int) -> int:
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

        # base case
        if  n == 0 or n == 1:
            return n
        
        # recursive case
        return self.fib(n-1) + self.fib(n-2)