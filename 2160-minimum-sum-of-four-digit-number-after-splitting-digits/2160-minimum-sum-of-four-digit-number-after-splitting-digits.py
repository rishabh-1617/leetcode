class Solution:
    def minimumSum(self, num: int) -> int:
        l = list(str(num))
        m1 = min(l)
        l.remove(m1)
        m2 = min(l)
        l.remove(m2)
        d1 = int(m1 + l[0])
        d2 = int(m2 + l[1])
        return d1 + d2