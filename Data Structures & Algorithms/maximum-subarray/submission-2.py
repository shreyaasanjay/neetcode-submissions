class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # basic idea: kadane's algo
        #so basically we have a left and right pointer and as long as the runningsum is >0, we increase right and this goes on until right is greater than len(nums)

        
        right = 0
        maxsum = max(nums)
        runningsum = nums[0]

        if len(nums)==1:
            return nums[0]

        while right<len(nums)-1:
            
            #print("right is " + str(right))
            #print("running sum is " + str(runningsum))
            if runningsum>0:
                #print("moved right forward by 1")
                right+=1
                runningsum+=nums[right]
            else:
                #print("restart the running sum")
                right+=1
                runningsum=nums[right]
            
            if runningsum>maxsum:
                maxsum=runningsum

        return maxsum


