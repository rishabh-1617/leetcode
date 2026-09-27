class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        ans = 0 

        for account in accounts:
            ans = max(sum(account),ans)
        return ans    