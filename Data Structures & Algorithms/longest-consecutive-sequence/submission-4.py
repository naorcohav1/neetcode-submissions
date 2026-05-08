class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        con_set = set(nums)
        current = 1
        count = 1
        for num in con_set:
            if num-1 not in con_set:
                next_num = num+1
                while next_num in con_set :
                    next_num += 1 
                    current +=1
                    if current > count:
                        count = current
                current = 1
        return count 
