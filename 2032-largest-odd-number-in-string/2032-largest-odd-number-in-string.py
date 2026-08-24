class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
        return ""        


       #digit = int(num)
       #l = [int(i) for i in str(num)]
       #if digit % 2 != 0:
        #s = str(digit)
        #return s

       #odd = [x for x in l if x % 2 != 0]
       #if odd:
        #largest = max(odd)
        #return str(largest)
       #else:
        #return "" """