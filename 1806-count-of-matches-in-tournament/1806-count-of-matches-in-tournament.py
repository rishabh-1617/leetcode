class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            rev = n // 2
            ans += rev
            n = n - rev
        return ans    

        """return n-1 """


