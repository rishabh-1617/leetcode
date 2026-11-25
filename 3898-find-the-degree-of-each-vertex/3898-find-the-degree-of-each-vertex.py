class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        
        d = []
        for i in matrix:
            d.append(i.count(1))
        return d