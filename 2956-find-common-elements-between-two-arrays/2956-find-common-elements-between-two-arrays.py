class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        left = 0
        right = 0

        for i in nums1:
            if i in nums2:
                left += 1
        
        for j in nums2:
            if j in nums1:
                right += 1
        
        return [left, right]
        # Using SET
        """
        set1 = set(nums1)
        set2 = set(nums2)

        left = sum(1 for x in nums1 if x in set2)
        right = sum(1 for x in nums2 if x in set1)

        return [left, right]
        """