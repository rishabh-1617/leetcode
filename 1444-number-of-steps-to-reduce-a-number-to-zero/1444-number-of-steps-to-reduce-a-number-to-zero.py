class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        temp = num
        while temp > 0:
            if temp % 2 == 0:
                temp //= 2
            else:
                temp -= 1
            count += 1    
        return count