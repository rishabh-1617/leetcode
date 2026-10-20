class Solution:
    def maxDistinct(self, s: str) -> int:

        # First Try
        #return len(set(s))

        seen = set()
        count = 0
    
        for char in s:
            if char not in seen:
                seen.add(char)
                count += 1
        return count
