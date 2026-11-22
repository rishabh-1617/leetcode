class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
        
        """
        set1 = set(nums1)
        set2 = set(nums2)

        list1 = [x for x in set1 if x not in set2]
        list2 = [x for x in set2 if x not in set1]

        return [list1, list2]
        """