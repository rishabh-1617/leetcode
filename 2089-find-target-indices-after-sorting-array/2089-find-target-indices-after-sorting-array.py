class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2
            
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        ans = []

        while i < len(nums) and nums[i] == target:
            ans.append(i)
            i += 1

        return ans    

        return ans                