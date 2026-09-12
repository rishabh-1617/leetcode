class Solution:
    def validDigit(self, n: int, x: int) -> bool:
       
       for i in str(n):
        if int(i) == x :
            if int(i) != int(str(n)[0]):
                return True
       return False    