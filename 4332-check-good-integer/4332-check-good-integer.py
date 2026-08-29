class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        d = 0
        s = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            d += digit
            s += digit * digit
            temp //= 10
        if (s - d) >= 50:
            return True
        else:
            return False    