class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Using MAP 
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]

            if need in seen:
                return [seen[need], i]
            seen[nums[i]] = i
        return [-1, -1]       

        """ BRUTE FORCE        
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [-1,-1] 
        """        