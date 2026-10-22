class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # FIRST aaproach
        """
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
        """
        #using Bucket Sort
        # counting frequencies
        freq = {} 
        for i in nums:
            freq[i] = freq.get(i, 0)+1
        # create buckets where index = frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
        # check from most freqency towards least 
        ans = []
        for j in range(len(bucket)-1, -1, -1):
            for num in bucket[j]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        return ans



        