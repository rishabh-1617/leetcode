class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        start = 0
        
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                """
                nums[i], nums[start] = nums[start], nums[i]
                start +=1"""
                temp = nums[i]
                nums[i] = nums[start]
                nums[start] = temp
                start += 1
        return nums        