class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        if num1 == num2:
            return 1
        ans = 0
        while num1 != num2:
            while num1 > num2:
                num1 -= num2
                ans += 1
            while num2 > num1:
                num2 -= num1
                ans += 1
        return ans + 1                    


        

            
        
        