class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_counter = 0
        for num in nums:
            if num != 0:
                total *=num
            else: 
                zero_counter +=1
        for index,num in enumerate(nums):
            if num != 0:
                if zero_counter > 0:
                    nums[index] = 0
                else:
                    nums[index] = int(total/num)
            else:
                if zero_counter == 1:
                    nums[index] = total
        return nums