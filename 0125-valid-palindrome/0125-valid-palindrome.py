class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join(e for e in s if e.isalnum()).lower()

        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True    