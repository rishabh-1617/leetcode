class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        ans = []
        
        for num in nums:
            sq = (num*num)
            ans.append(sq)
        return sorted(ans)