class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
    
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)
        #BRUTE FORCE
        """
        mp = {}
        for num in nums1:
            mp[num] = mp.get(num, 0) + 1
        
        result = []
        for num in nums2:
            if num in mp:
                result.append(num)
                del mp[num]
        
        return result
        """