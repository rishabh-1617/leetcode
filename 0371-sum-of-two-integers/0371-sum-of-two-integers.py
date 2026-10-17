import ctypes
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a = ctypes.c_int32(a).value
        b = ctypes.c_int32(b).value
        while b != 0:
            sum_without_carry = ctypes.c_int32(a ^ b).value
            carry = ctypes.c_int32((a & b) << 1).value
            
            a = sum_without_carry
            b = carry
        return a    

        """ For +ve numbers only
        if b == 0:
            return a
        carry = a & b    
        return self.getSum(a ^ b, carry << 1)    
        """