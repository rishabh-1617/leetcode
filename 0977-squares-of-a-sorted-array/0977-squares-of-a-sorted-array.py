class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Brute Force
        """
        ans = []
        
        for num in nums:
            sq = (num*num)
            ans.append(sq)
        return sorted(ans)
        """
        # TWO POINTER
        n = len(nums)
        i = 0
        j = n - 1
        res = [0] * n

        for x in range(n-1,-1,-1):
            if abs(nums[i]) > abs(nums[j]):
                res[x] = nums[i] ** 2
                i += 1
            else:
                res[x] = nums[j] ** 2
                j -= 1
        
        return res
        
        

