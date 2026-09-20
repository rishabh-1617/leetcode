class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
        """
        has_all_letters = True
        for ascii_code in range(97,123):
            letter = chr(ascii_code)
            if letter not in sentence:
                has_all_letters = False
                return False
            
        return True"""