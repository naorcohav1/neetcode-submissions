class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if dic.get(num) is not None:
                return True
            dic[num] = 0
        return False