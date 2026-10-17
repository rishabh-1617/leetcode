class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        # Using TWO Pointers
        for word in words:
            if self.ispalindrome(word): # function call
                return word
        return ""       

    def ispalindrome(self, s):   
        left = 0
        right = len(s) - 1
            
        while left < right: 
            if s[left] != s[right]: #check
                return False    
            left += 1
            right -= 1
                  
        return True   

        """
        for word in words:
            if word == word[::-1]:
                return word
        return ""
        """     
