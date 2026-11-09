class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        n = len(grid)
        count = [0] * (n*n+1
        )
        for row in grid:
            for i in row:
                count[i] += 1
        
        missing = []
        repeated = []

        for i in range(1, n*n+1):
            if count[i] == 0:
                missing.append(i)
            elif count[i] > 1:
                repeated.append(i)

        return repeated + missing