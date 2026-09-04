class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Optimized
        temp = sorted(nums)
        mapping = {}
        ans = []
        for i in range(len(temp)):
            if temp[i] not in mapping:
                mapping[temp[i]] = i
        for i in range(len(nums)):
            ans.append(mapping[nums[i]])
        return ans       

        # Brute Force
        """
        ans = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            ans.append(count)
        return ans            """