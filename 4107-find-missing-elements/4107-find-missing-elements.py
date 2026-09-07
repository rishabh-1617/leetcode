class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # Optimal
        s = set(nums)
        ans = []
        for i in range(min(nums),max(nums)+1):
            if i not in s:
                ans.append(i)
        return ans        
        """arr = sorted(nums)
        mn = min(nums)
        mx = max(nums)
        ans = []
        for i in range(mn,mx+1):
            found = False
            for j in arr:
                if i == j:
                    found = True
                    break
            if not found:
                ans.append(i)   
        return ans     """        