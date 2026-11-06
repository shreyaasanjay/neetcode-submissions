class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #sliding window ig 
        #ok so for each value, the total area is max (height1, height2) * diff btwn the two x values 
        #idea is to make it o(n), we only check each value once 
        #so when the left value is smaller, we know that its holding it back, so we move left by 1 to try to find a better height, but if right is smaller than we move right back by 1? so we essentially check each height once

        left = 0
        right = len(heights)-1
        maxarea = 0
        while left<len(heights)-1 and left<=right:   
            maxarea = max((min(heights[right], heights[left]) * (right-left), maxarea))
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        
        return maxarea








