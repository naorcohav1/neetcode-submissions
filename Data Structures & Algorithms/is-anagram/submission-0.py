class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s = {}
        for char in s:
            if dic_s.get(char) is None:
                dic_s[char] = 1
            else:
                dic_s[char] += 1
         
        for char in t:
            if dic_s.get(char) is None:
                return False
            else: 
                dic_s[char] -=1
        
        for value in dic_s:
            if dic_s[value] > 0:
                return False
        return True
