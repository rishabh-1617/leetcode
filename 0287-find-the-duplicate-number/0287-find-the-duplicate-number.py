class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Binary Search : TC - O(n log n ) and SC - O(1) 
        i = 1
        j = len(nums) - 1

        while i < j:
            mid = i+(j-i) // 2
            count = 0

            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                j = mid
            else:
                i = mid + 1

        return i               
        
        # Brute Force : TC - O(n log n) and SC - O(log n)
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
        """
        

            

