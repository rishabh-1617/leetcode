class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0 
        while n > 0:
            n //= 5
            cnt += n
        return cnt    
        """fact = 1  Brute Force
        if n == 0:
            return 0
        for i in range(2,n+1):
            fact *= i
        temp = fact
        count = 0
        while temp > 0:
            if temp % 10 == 0:
                count += 1
                temp //= 10
            else:
                break
        return count"""   


        