class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10
        alice = True

        while take > 0:

            if n < take:
                return not alice

            n -= take
            take -= 1
            alice = not alice    
