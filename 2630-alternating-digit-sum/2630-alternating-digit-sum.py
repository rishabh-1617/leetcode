class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        for i,digit in enumerate(str(n)):
            if i % 2 == 0:
                total += int(digit)
            else:
                total -= int(digit)
        return total            
        """ Using Range 
        n_str = str(n)
        for i in range(len(n_str)):
            if i % 2 == 0:
                total += int(n_str[i])
            else:
                total -= int(n_str[i])
        return total  """        