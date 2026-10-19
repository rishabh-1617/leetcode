class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        i = 1
        j = len(nums) - 1

        while i < j:
            mid = i+(j-i) // 2
        """
        nums.sort()
        i = 0
        j = i + 1

        while j < len(nums):

            if nums[i] == nums[j]:
                return nums[i]

            i += 1
            j += 1   
             
        return -1   
            
        

            

