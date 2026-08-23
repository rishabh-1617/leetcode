class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for j in range(k):
            
            s = min(nums)
            i = nums.index(s)
            nums[i] = nums[i] * multiplier
    
        return nums