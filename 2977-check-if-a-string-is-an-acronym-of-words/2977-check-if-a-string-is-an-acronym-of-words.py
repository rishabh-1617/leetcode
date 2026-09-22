class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        first_char = ""
        for i in words:
            first_char += i[0]
        return first_char == s    