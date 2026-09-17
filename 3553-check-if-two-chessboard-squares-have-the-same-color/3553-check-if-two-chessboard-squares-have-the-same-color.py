class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1 = ord(coordinate1[0])
        r1 = ord(coordinate1[1])
        c2 = ord(coordinate2[0])
        r2 = ord(coordinate2[1])
        return (c1 + r1) % 2 == (c2 + r2) % 2