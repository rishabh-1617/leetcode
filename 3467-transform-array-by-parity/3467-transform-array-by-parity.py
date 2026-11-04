class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # Brute Force
        """
        ans = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                ans.append(0)
            else:
                ans.append(1)
        
        return sorted(ans)
        """
        # using Two Pointers
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[j] = 0
                j += 1

        while j < len(nums):
            nums[j] = 1
            j += 1
            
        return nums
