class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        major = n // 2
        freq = {}

        for i in nums:
            # update frequency in dict
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
            # immediate check of majority element
            if freq[i] > major:
                return i       

        return -1              
                
