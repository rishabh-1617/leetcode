class Solution:
    def reverseByType(self, s: str) -> str:
        n = len(s)
        low = 0
        high = n - 1
        s = list(s)

        while low < high:
            if 97 <= ord(s[low]) <= 122 and 97 <= ord(s[high]) <= 122 :
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1
            elif ord(s[low]) < 97 or ord(s[low]) > 122:
                low += 1
            else:
                high -= 1
        
        i, j = 0, n - 1
        while i < j:
            if (ord(s[i]) < 97 or ord(s[i]) > 122) and (ord(s[j]) < 97 or ord(s[j]) > 122):
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif 97 <= ord(s[i]) <= 122:
                i += 1
            else:
                j -= 1
            
        return "".join(s)

