class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        ans = 0
        max_range = -1
        for i in nums:
            temp = i
            l = 0
            s = 9
            while temp > 0:
                d = temp % 10
                l = max(l,d)
                s = min(s,d)
                temp //= 10
                
                digit_range = l - s
          
            if digit_range > max_range:
                max_range = digit_range
                ans = i
            elif digit_range == max_range:
                ans += i
        return ans    








