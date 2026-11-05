class Solution:
    def sortSentence(self, s: str) -> str:
        word = s.split()
        result =[""] * len(word)
        for w in word:
            postion = int(w[-1])
            result[postion - 1] = w[:-1]
        
        return " ".join(result)