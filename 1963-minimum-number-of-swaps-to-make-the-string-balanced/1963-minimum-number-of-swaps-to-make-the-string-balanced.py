class Solution:
    def minSwaps(self, s: str) -> int:
        
        
        n = len(s)
        if n == 2:
            return 0
        res = 0
        for bra in s:
            if bra == '[':
                res += 1
            elif res > 0:
                res -= 1
        return (res + 1) // 2
            




        
            