class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        total_1 = sum(nums)
        comp = list(range(1,n+1))
        total_2 = sum(comp)
        
        return total_2 - total_1