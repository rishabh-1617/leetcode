class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        s = min(nums)
        l = max(nums)
        hcf = 1                               # Euclidean Algorithm for GCD
        for i in range(1,s + 1):              # while l != 0:
            if (s % i == 0) and (l % i == 0): #      s, l = l, s % l
                hcf = i                       # return s
        return hcf