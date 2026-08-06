class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def game(n, k):
            if n == 1:
                return 0
            return (game(n - 1, k) + k) % n

        return game(n, k) + 1

        """ win = 0
        for i in range (1, n + 1):
            win = (win + k) % i
        return win + 1 """  