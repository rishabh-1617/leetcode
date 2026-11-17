class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        for i in t:
            if s.count(i) != t.count(i):
                return i
        """
        S = list(s)
        T = list(t)
        for c in S:
            T.remove(c)
        return T[0]