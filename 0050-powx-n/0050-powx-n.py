class Solution:
    def findpow(self,x,n):
        # Base case
        if n == 0:
            return 1
        # Recursive case
        a = self.findpow(x,n//2)
        if n%2 == 0:
            return a*a
        else:
            return a*a*x    
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.findpow(x,n)
        else:
            return 1/self.findpow(x,n*(-1))    
        