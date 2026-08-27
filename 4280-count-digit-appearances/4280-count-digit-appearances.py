class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for x in nums:
            temp = x

            while temp > 0:
                d = temp % 10

                if d == digit:
                    count += 1

                temp //= 10
        return count