class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        f = -1
        l = -1
        for index,n in enumerate(nums):
            if n < 2:
                continue
            count = 1
            for i in range(1,isqrt(n)+1):
                if n % i == 0:
                    count += 1
            if count == 2:
                if f == -1:
                    f = index
                l = index    
        return l - f 
        """
        arr = []
        for index,n in enumerate(nums):
            count = 1
            for i in range(1,isqrt(n)+1):
                if n % i == 0:
                    count += 1
            if count == 2:
                arr.append(index)
        ans = max(arr) - min(arr)
        return ans        
        """
                           