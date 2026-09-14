class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            p = 1
            for c in str(n):
                p *= int(c)
            if p % t == 0:
                return n
            n += 1

        """
        def productOfDigits(temp):
            p = 1
            while temp:
                digit = temp % 10
                p *= digit
                temp //= 10
            return p    
        while productOfDigits(n) % t != 0:
            n += 1
        return n    
        """