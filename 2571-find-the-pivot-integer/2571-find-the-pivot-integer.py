class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = list(range(1,n+1))
        """
        for i in arr:
            left = sum(arr[:i-1])
            right = sum(arr[i:])
            if left == right:
                return i
        return -1
        """
        total = n * (n + 1) // 2
        x = int(total ** 0.5)

        if x * x == total:
            return x

        return -1