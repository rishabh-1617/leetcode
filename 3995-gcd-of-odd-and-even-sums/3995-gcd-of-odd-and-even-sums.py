class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0

        for i in range(1,n*2,1):
            if i % 2 != 0:
                sumOdd += i
            else:
                sumEven += i 

        return math.gcd(sumOdd, sumEven)