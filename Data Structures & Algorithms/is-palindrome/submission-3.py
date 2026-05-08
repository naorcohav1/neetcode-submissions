class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start < end:
            while start < end and not is_english_alnum(s[start]):
                start +=1
            while start < end and not is_english_alnum(s[end]):
                end -=1

            if s[start].lower() != s[end].lower():
                return False
            else :
                start +=1
                end -=1

        return True

def is_english_alnum(char):
    return (
        'a' <= char <= 'z' or 
        'A' <= char <= 'Z' or 
        '0' <= char <= '9'
    )