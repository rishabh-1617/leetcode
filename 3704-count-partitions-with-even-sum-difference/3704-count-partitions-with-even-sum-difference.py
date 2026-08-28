class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        #Optimal
        if sum(nums) % 2 == 0:
            return len(nums) - 1
        else:
            return 0    

        #Brute Force     
        """left = []
        right = []
        count = 0
        for i in range(0,len(nums) -1):

            left = nums[:i+1]
            right = nums[i+1:]
            x = sum(left)
            y = sum (right)
            if (y - x) % 2 == 0:
                count += 1
        return count    """