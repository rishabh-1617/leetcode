class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)
        for i in range(-1,-n-1,-1):
            if s[i] == " " :
                return -i-1
        return n             