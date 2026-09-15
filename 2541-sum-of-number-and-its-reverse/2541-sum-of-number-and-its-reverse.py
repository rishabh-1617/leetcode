class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True
        
        for i in range(num//2,num+1):
            original = str(i)
            rev = str(original)[::-1]
            if int(original) + int(rev) == num:
                return True
        return False
