class Solution:
    def reversePrefix(self, s: str, k: int) -> str:

        if k == len(s):
            return s[::-1]

        st = ""
        for i in range((k-1),-1,-1):
            st += s[i]
        return st + s[k:]    
