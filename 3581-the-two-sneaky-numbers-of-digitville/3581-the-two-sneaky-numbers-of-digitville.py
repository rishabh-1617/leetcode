class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        seen = set()
        dup = set ()

        for i in nums:
            if i in seen:
                dup.add(i)
            else:
                seen.add(i)
        return list(dup)            