class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        start = 0

        for i in range(1,len(nums)):
            #Unique Element
            if nums[start] != nums[i]:
                start += 1
                nums[start] = nums[i]
        return start + 1        