class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        # Brute Force
        """
        count = 0
        for char in stones:
            for ch in jewels:

                if char == ch:
                    count += 1

        return count 
        """     
        # Using HashSet
        seen = set(jewels)
        count = 0

        for ch in stones:
            if ch in seen:
                count += 1

        return count
            