class Solution:
    def removeZeros(self, n: int) -> int:
        s = int(str(n).replace('0',''))
        return s
        """
        ans = 0
        place = 1
        while n:
            digit = n % 10
            if digit:
                ans += digit * place
                place *= 10
            n //= 10
        return ans   """     
