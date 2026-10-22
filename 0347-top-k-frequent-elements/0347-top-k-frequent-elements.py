class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # FIRST aaproach
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        ans = []
        for j in range(k):
            m = max(freq, key = freq.get)
            ans.append(m)
            freq.pop(m)

        return ans



        