class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start,end,current,max = 0,len(heights) - 1,0,0
        while start < end:
            current = min(heights[start],heights[end]) * (end-start)
            if current > max:
                max = current
            if heights[start] > heights[end]:
                end -=1
            else:
                start+=1
        return max
