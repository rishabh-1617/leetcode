class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        curr_sum = 0

        # sum of the first window
        for i in range(k):
            curr_sum += nums[i]

        max_avg = curr_sum / k

        # slide the window one step at a time
        for i in range(k, n):
            curr_sum += nums[i]      # new element enters
            curr_sum -= nums[i - k]  # old element leaves

            avg = curr_sum / k
            max_avg = max(max_avg, avg)

        return max_avg
