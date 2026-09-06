class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        """
        x = set()
        for i in nums:
            if i in x:
                return True
            x.add(i)    
        return False """    