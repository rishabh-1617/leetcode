class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        # Using Binear Search - (Divide & Conquer)
        count = 0
        for row in grid:
            low = 0
            high = len(row) - 1
            row = sorted(row)
            for element in row:
                mid = (low + high) // 2
                if row[mid] < 0:
                    low += 1
                    count += 1
                else:
                    high -= 1    

        return count            

        # Brute Force
        """
        count = 0
        for row in grid:
            for element in row:
                if element < 0:
                    count += 1

        return count            
        """