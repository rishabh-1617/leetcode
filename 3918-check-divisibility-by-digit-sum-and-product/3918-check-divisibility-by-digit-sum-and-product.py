class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        temp = n
        while temp > 0:
            digit = temp % 10
            s += digit
            p *= digit
            temp //= 10
        Sum = s + p
        if n % Sum == 0:
            return True
        else:
            return False        