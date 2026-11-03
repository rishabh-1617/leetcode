class Solution:
    def minMoves(self, nums: List[int]) -> int:

        return max(nums) * len(nums) - sum(nums)
        """
        count = 0
        mx = max(nums)
        for i in range(len(nums)):
            count += mx - nums[i]
        
        return count
        """