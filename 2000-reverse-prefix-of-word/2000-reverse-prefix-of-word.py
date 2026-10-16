class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        

        for i in range(n):
            if word[i] == ch:
                str1 = word[:i+1]
                str2 = word[i+1:]
                return str1[::-1] + str2   
                
        return word        