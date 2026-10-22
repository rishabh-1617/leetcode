class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        seen = set(nums)
        count = 0

        for i in seen:

            if (i - 1) not in seen:
                streak = 1

                while (i + streak) in seen:
                    streak += 1
                    
                count = max(count,streak)        

        return count        

        