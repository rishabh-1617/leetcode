class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
    
        return (
            [n for n in nums if n < pivot] +
            [n for n in nums if n == pivot] +
            [n for n in nums if n > pivot]
        )
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
    