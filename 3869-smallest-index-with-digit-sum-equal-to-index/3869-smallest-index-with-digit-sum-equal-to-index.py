class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(map(int,str(nums[i]))) == i:
                return i
        return -1        
        
        """ Brute Force - O(n ** 2)
        for i in range(len(nums)):
            temp = nums[i]
            s = 0
            while temp > 0:
                digit = temp % 10
                s += digit
                temp //= 10
            if s == i:
                return i
        return -1    """

