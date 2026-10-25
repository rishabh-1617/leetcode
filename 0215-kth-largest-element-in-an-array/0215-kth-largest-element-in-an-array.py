import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Using sorting
        """
        nums.sort()
        return nums[-k]
        """
        
        # Using HEAP
        h = []

        for x in nums:
            heapq.heappush(h, x)
            if len(h) > k:
                heapq.heappop(h)
        
        return h[0]
