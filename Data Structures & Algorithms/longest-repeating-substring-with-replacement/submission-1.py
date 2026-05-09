class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        letters = {}
        max_freq = 0
        max_length = 0
        
        for right in range(len(s)):
            char = s[right]
            letters[char] = letters.get(char, 0) + 1
            
            max_freq = max(max_freq, letters[char])
            
            while (right - left + 1) - max_freq > k:
                letters[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            
        return max_length