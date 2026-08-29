class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        Sum = 0
        
        for ch in str(x):
            Sum += int(ch)
        if x % Sum == 0:
            return Sum
        else:
            return -1    