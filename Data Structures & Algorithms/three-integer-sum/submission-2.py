class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # מיון הוא חובה ל-Two Pointers
        
        for i in range(len(nums)):
            # דילוג על כפילויות עבור המצביע הראשון i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # עבור כל i, אנחנו מאתחלים מחדש את המצביעים
            # left מתחיל מיד אחרי i, ככה הם לעולם לא יתנגשו ולא צריך לבדוק if i == left
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # עכשיו חייבים לקדם את המצביעים
                    left += 1
                    right -= 1
                    
                    # דילוג על כפילויות עבור left ו-right כדי לא לקבל אותה שלשה שוב
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return res