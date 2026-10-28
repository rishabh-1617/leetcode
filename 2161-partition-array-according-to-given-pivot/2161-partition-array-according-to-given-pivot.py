class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less = []
        high = []
        count = 0

        for num in nums:

            if num < pivot:
                less.append(num)
            elif num == pivot:
                count += 1
            else:
                high.append(num)
                
        return less + [pivot] * count + high


        
        # Four Pointer
        """
        n = len(nums)
        low = 0
        high = n - 1
        ans= [0] * n
        i = 0
        j =  n-1
        while i < n:

            if nums[j] > pivot:
                ans[high] = nums[j]
                high -= 1
            if nums[i] < pivot:
                ans[low] = nums[i]
                low += 1
            
            i += 1
            j -= 1
        
        while low <= high:
            ans[low] = pivot
            low += 1
        return ans   

        """
    