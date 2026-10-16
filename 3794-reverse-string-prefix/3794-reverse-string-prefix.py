class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return ''.join([s[k - 1::-1],s[k:]])
        """
        # Swapping
        s = list(s)

        for i in range(k//2):
            s[i], s[k-1-i] = s[k-1-i], s[i]

        return "".join(s)    
        """
        """ Brute Force
        if k == len(s):
            return s[::-1]

        st = ""
        for i in range((k-1),-1,-1):
            st += s[i]
        return st + s[k:]    
        """