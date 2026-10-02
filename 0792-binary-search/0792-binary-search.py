class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Linear Search 
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1  
        """      
        # Binary Search
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid] :
                return mid
            elif target > nums[mid]:
                #right side
                l = mid + 1
            else:
                #left side
                r = mid - 1        
        return -1        
