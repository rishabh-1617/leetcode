class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        """
        min_avg = float('inf')
        nums.sort()
        j = len(nums) - 1

        for i in range(len(nums) // 2):
            avg = (nums[i] + nums[j]) / 2.0
            min_avg = min(avg, min_avg)
            j -= 1

        return min_avg
        """
        nums.sort()
        i = 0
        j = len(nums) - 1
        ans = float("inf")

        while i < j:
            avg = (nums[i]+nums[j]) / 2
            
            ans = min(ans, avg)
            i += 1
            j -= 1
        
        return ans
