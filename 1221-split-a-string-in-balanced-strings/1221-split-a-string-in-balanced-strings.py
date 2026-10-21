class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        count = 0
        cnt = 0
        for i in range(len(s)):

            if s[i] == 'R':
                cnt += 1
            else:
                cnt -= 1

            if cnt == 0:
                count += 1

        return count         