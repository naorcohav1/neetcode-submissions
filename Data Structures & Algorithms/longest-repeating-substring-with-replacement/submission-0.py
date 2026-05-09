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
            
            # 3. בדיקה: האם מספר התווים שצריך להחליף גדול מ-k?
            # אורך החלון פחות התו הנפוץ ביותר
            while (right - left + 1) - max_freq > k:
                # החלון לא תקין! מצמצמים משמאל
                letters[s[left]] -= 1
                left += 1
                # הערה: לא חייבים לעדכן את max_freq כאן, זה יעבוד גם בלי
            
            # 4. עדכון התוצאה המקסימלית
            max_length = max(max_length, right - left + 1)
            
        return max_length