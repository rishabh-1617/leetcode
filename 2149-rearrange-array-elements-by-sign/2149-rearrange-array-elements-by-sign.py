class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        ans = [0] * len(nums)
        p = 0
        n = 1

        for num in nums:
            #checking +ve or -ve
            if num > 0:
                ans[p] = num 
                p += 2 #place at +ve element index
            else:
                ans[n] = num
                n += 2

        return ans