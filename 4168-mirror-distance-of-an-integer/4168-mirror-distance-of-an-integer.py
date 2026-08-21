class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        og = n
        while n > 0 :
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10
        
        return abs(og - rev)