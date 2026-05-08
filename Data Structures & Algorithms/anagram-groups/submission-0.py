class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        for string in strs:
            string_key = "".join(sorted(string))
            if string_key not in sets:
                sets[string_key] = []
            sets[string_key].append(string)   
        return list(sets.values()) 