class Solution:
    def isFascinating(self, n: int) -> bool:
        
        num = str(n) + str(2 * n) + str(3 * n)
        
        return len(num) == 9 and set(num) == set("123456789")

        #return "".join(sorted(str(num))) == "123456789"
        
            