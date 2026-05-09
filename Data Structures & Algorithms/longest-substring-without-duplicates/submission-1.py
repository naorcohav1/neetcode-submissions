class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # אם האות כבר קיימת, נצמצם את החלון משמאל
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # עכשיו בטוח שאין כפילות, אפשר להוסיף את האות
            char_set.add(s[right])
            
            # חישוב אורך החלון הנוכחי ועדכון המקסימום
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)
            
        return max_length