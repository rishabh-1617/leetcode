class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10: return False
        if n < 19: return True
        if n < 27: return False
        if n < 34: return True
        if n < 40: return False
        if n < 45: return True
        if n < 49: return False
        
        return True
        """
        for stones in (19, 15, 11, 7, 3):

            if n >= stones: 
                n-= stones
               
            else: return n >= stones//2 +1

        return True
        """