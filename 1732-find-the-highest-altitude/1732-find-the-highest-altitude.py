class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        
        arr = [0] * (len(gain) + 1)
        arr.append(0)

        for i in range(1,len(gain)+1):
            arr[i] = arr[i-1] + gain[i-1]

        return max(arr)