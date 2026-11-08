class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        vowels = "aeiou"
        consonants = "qwrtyupsdfghjklzxcvbnm"
        
        freq1 = dict.fromkeys(vowels, 0)
        freq2 = dict.fromkeys(consonants, 0)

        for char in s:
            if char in freq1:
                freq1[char] += 1
            else:
                freq2[char] += 1

        return max(freq1.values()) + max(freq2.values())