class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        def is_prime(i):
            if i <= 1:
                return False
            if i == 2:
                return True
            if i % 2 == 0:
                return False
            for num in range(3,int(i**0.5)+1,2):
                if i % num == 0:
                    return False
            return True
        ans = 0
        for i in range(min(n,r),max(r,n)+1):
            if is_prime(i):
                ans += i
        return ans        