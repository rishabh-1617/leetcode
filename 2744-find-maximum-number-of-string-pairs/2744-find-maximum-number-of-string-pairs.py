class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        ans = 0
        seen = set()
        for word in words:
            if word in seen:
                ans += 1
            else:
                seen.add(word[::-1])
        return ans
            