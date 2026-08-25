class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        binary = bin(n)[2:]
        original = binary
        binary = int(binary)
        rev = 0
        while binary > 0:
            d = binary % 10
            rev = rev * 10 + d
            binary //= 10
            if original == rev:
                return True
            else:
                return False    
        