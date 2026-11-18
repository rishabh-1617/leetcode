class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        return sorted(nums, key = lambda x: (freq[x], -x))

