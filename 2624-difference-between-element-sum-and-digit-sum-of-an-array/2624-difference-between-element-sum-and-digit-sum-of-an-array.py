import sys
sys.set_int_max_str_digits(10000)

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        digit = int("".join(map(str,nums)))

        s = 0 
        temp = digit
        while temp > 0:
            d = temp % 10
            s += d
            temp //= 10
        y = sum(nums)
        return abs(s - y)   