class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        # Binary Search O(n log max(nums))
        left = max(1,(sum(nums) + threshold - 1) // threshold)
        right = max(nums)
        
        while left < right:
            mid = (left + right) // 2
            res = 0
            for i in nums:
                res += (i + mid - 1) // mid # round off
                
                if res > threshold:
                    break

            if res <= threshold: 
                right = mid
            else:
                left = mid + 1

        return left                
        
        # Brute Force O(n square)
        """
        for i in range(1,max(nums)+1):
            res = 0
            for j in nums:
                
                res += (j + i - 1) // i 

            if res <= threshold:
                return i

        return max(nums)
        """

