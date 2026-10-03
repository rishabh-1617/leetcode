class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # TWO POINTERS
        n = len(nums)
        left = 0 
        right = n - 1
        mid = 0

        while mid <= right:
            if nums[mid] == 0:
                temp = nums[mid]
                nums[mid] = nums[left]
                nums[left] = temp
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                temp = nums[mid]
                nums[mid] = nums[right]
                nums[right] =  temp
                right -= 1      
        """ BRUTE FORCE
        zero = one = two = 0
        for n in nums:
            if n == 0:
                zero += 1
            elif n == 1:
                one += 1
            else:
                two += 1

        for i in range(len(nums)):
            if zero > 0:
                nums[i] = 0
                zero -= 1
            elif one > 0:
                nums[i] = 1
                one -= 1
            else:
                nums[i] = 2
                two -= 1
                """