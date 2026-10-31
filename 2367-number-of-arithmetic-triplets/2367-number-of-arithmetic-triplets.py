class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:

        # Using Three Pointer Brute Force
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        cnt += 1
        
        return cnt
        """
        # Using hashset

        s = set(nums)
        cnt = 0
        for num in nums:
            if num + diff in s and num + 2 * diff in s:
                cnt += 1
        return cnt