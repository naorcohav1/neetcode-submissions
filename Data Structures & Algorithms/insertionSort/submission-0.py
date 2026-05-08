class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        
        if len(pairs) == 0:
            return res
            
        for i in range(len(pairs)):
            j = i
            
            while j > 0 and pairs[j - 1].key > pairs[j].key:
                pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                j -= 1
            
            res.append(pairs[:])
            
        return res