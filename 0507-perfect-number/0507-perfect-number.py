class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Optimal Approach
        if num <= 1:
            return False
        ans = 1
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                ans+=i
                if i*i != num:
                    ans+=num//i

        return ans == num      
                           
        # BRUTE FORCE
        """if num % 2 != 0: BRUTE FORCE
            return False
        x = 0
        for i in range(1,num):
            if num % i == 0:
                x += i
        return num == x           """

