class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Optimal
        return (high+1)//2 - low//2