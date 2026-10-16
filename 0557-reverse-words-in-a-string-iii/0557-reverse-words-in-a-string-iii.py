class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        left = 0
        
        for right in range(len(chars)+1):
            # space check
            if right == len(chars) or chars[right] == " ":
                l, r = left, right - 1
                # Swap the characters of each word
                while l < r: 
                    chars[l], chars[r] = chars[r], chars[l]
                    l += 1
                    r -= 1
                # moves to the next word
                left = right + 1

        return "".join(chars)