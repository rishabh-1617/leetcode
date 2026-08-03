class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        '''return sum([math.comb(n, 2) for n in collections.Counter(nums).values()])'''
                
        count = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    count += 1
        
        return count 