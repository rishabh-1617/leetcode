class Solution:
    def checkString(self, s: str) -> bool:
        
        return "ba" not in s

        # Adjacent Pair Check
        """
        for i in range(len(s) - 1):
            if s[i] == 'b' and s[i + 1] == 'a':
                return False

        return True
        
        # Flag single pass
        seen_b = False

        for ch in s:
            if ch == 'b':
                seen_b = True
            elif seen_b:
                return False

        return True

        """