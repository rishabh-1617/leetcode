class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = 0
        max_sum = nums[0] #Kadane's Algo

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0   

        return max_sum         
