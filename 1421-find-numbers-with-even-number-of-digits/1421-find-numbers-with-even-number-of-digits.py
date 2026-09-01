class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            temp = nums[i]
            count = 0
            digit = 0
            while temp > 0:
                digit = temp % 10
                count += 1
                temp //= 10
            if count % 2 == 0:
                c += 1
        return c        
                