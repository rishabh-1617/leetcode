class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rightsum = sum(nums)
        leftsum = 0
        ans =[0] * len(nums)

        for i in range(len(nums)):

            rightsum -= nums[i]
            ans[i] = abs(leftsum - rightsum)
            leftsum += nums[i]

        return ans