class Solution:
    def countEven(self, num: int) -> int:
        current = 0
        i = num
        while i:
            current += i % 10
            i //= 10
        if current % 2 == 0:
            return num // 2
        else:
            return (num - 1) // 2        

        """ Brute Force
        count = 0
        for i in range(1,num+1):
            temp = i
            s = 0
            while temp > 0:
                digit = temp % 10
                s += digit
                temp //= 10
            if s % 2 == 0 :
                count += 1    
        return count        """
