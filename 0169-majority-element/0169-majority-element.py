class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        major = n // 2
        freq = {}

        for i in nums:

            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

            if freq[i] > major:
                return i       

        return -1              
                
