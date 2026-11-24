class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        """
        rev = nums[::-1]
        return nums + rev
        """
        
        for i in range(len(nums)-1, -1, -1):
            nums.append(nums[i])
        
        return nums
