class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #   one pass stack solve

        # so basically u have one stack and then u add a height and index to the stack
        # and when if the next value has a bigger height, u continue to add to stack
        # if the next value is smaller, then that means u cant continue and pop that value
        # and calculate max area by using the pop index and the current i 


        stack = []
        maxarea = 0
        area = 0
        index=0
        popped = ()

        for i in range(len(heights)):
            index = i
            if len(stack)==0:
                stack.append(((heights[i]),index))
                #print("starting stack")
                if i>0:
                    area = (i - popped[1]) * popped[0]
                    #print("getting area when stack is zero")
                    if area>maxarea:
                        maxarea=area
                    

            else:
                #print("stack is not empty")
                #print(stack)
                     
                while stack and heights[i]<stack[-1][0]:
                    #print(stack)
                    popped = stack.pop()
                    area = (i - popped[1]) * popped[0]
                    #print("getting area")
                    #print(area)
                    index = popped[1]
                    if area>maxarea:
                        maxarea=area
                stack.append(((heights[i]),index))
                    #print("popped")
        
        for height in stack:
            area = (len(heights)-height[1]) * height[0]
            maxarea= max(area,maxarea)



        return maxarea


                

