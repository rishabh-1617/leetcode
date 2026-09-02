class Solution:
    def isPalindrome(self, x: int) -> bool:

        return str(x)==str(x)[::-1]

        """
        if x < 0:
            return False

        rev = 0
        num = x 
        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10
        return rev == x         """