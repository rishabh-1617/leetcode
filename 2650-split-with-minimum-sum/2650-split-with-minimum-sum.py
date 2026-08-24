class Solution:
    def splitNum(self, num: int) -> int:

        """s = ''.join(sorted(str(num)))
        return int(s[::2]) + int(s[1::2])"""

        num = list(str(num))
        num.sort()
        a = ""
        b = ""

        for i in range(len(num)):
            if i % 2 == 0:
                a += num[i]
            else:
                b += num[i]
        return int(a) + int(b)             