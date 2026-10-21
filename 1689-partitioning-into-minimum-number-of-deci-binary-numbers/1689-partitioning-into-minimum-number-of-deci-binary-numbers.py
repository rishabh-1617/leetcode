class Solution:
    def minPartitions(self, n: str) -> int:
        
        largest = 0
        for ch in n:

            if int(ch) > largest:
                largest = int(ch)

        return largest