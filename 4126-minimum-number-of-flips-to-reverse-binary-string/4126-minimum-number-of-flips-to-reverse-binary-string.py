class Solution:
    def minimumFlips(self, n: int) -> int:
        s = str(bin(n)[2:])
        rev = s[::-1]
        count = 0
        for i in range(len(s)):
            if s[i] != rev[i]:
                count += 1
        return count    
               
