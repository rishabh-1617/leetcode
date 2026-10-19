class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n = len(arr)
        i = 0
        j = n - 1

        while i < j:
            mid = (i + j) // 2
            # main logic is to check for the change in slope.
            if arr[mid] < arr[mid+1]:
                i = mid + 1
            else:
                j = mid

        return i            

        # Just Trna Out !!
        """
        peak = max(arr)
        return arr.index(peak)
        """