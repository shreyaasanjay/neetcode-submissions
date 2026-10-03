class Solution:
    def trap(self, height: List[int]) -> int:
        #use 2 pointers - the key idea is that we have left starting at zero
        #and right starting at the very end of height
        #then we also intialize a max left value and a max right value
        #then while left<right, we check if maxleft is less than max right, since we want
        #to get the minimum of those two values, subtract the height at that value and 
        #then we get the water we can put at that value
        
        if len(height)==0:
            return 0

        left = 0
        right = len(height)-1

        max_left = height[left]
        max_right = height[right]

        running_sum = 0

        while left<=right:
            if max_left<=max_right:
                if max_left - height[left]<0:
                    running_sum+=0
                else:
                    running_sum+=max_left - height[left]
                if height[left]>max_left:
                    max_left=height[left]
                left+=1 
            else:
                if max_right-height[right]<0:
                    running_sum+=0
                else:
                    running_sum+=max_right - height[right]
                if height[right]>max_right:
                    max_right=height[right]
                right-=1
        return running_sum

