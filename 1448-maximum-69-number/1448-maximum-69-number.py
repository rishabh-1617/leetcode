class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = [int(x) for x in str(num)]
        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break
            
        final = int("".join(map(str,digits)))        
        return final       