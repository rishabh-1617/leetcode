class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:

        n = len(code)
        ans = []
        
        for i in range(n):
            s = 0
            if k > 0:
                for j in range(1,k+1):
                    s += code[(i+j)%n]
                ans.append(s)
        
            elif k < 0:
                for j in range(1,abs(k)+1):
                    s += code[(i-j)%n]
                ans.append(s)
            else:
                ans.append(0)
        
        return ans
        