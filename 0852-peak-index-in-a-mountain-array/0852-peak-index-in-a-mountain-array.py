class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        
        peak = max(arr)
        return arr.index(peak)