class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        vol = 0
        nvol = 0

        while left<right and right<len(heights):
            nvol = abs(right-left) * min(heights[left], heights[right])
            if nvol>vol:
                vol=nvol
            
            if heights[left]>=heights[right]:
                right-=1

            else:
                left+=1
        return vol

