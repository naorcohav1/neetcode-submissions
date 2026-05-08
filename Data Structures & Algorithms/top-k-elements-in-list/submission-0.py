class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        sorted_keys = sorted(count.keys(), key=count.get, reverse=True)
        
        return sorted_keys[:k]