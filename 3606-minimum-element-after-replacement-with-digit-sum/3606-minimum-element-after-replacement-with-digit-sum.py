class Solution:
    def minElement(self, nums: List[int]) -> int:


        arr = []
        for i in nums:
            temp = i
            s = 0

            while temp > 0:
                d = temp % 10
                s += d
                temp //= 10
            
            arr.append(s)
        return min(arr)         
