class Solution:
    def firstMatchingIndex(self, s: str) -> int:

        right = len(s) - 1
        for i in range(len(s)):
            if s[i] == s[right - i]:
                return i 

        return -1        