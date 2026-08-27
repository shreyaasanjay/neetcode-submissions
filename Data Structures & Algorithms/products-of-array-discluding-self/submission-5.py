class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #in python for loopsu can do range(start, stop, step)
        #so if u wanna go backwards you have to do step = -1
        prefix = [1] * len(nums)
        suffix = [1]* len(nums)
        returnnums = [0] * len(nums)
        count = 0

        for i in range(len(nums)-2, -1,-1):   
            suffix[i] = suffix[i+1] * nums[i+1]
            

        for i in range(len(nums)):
            count = 0
            product = 1
            if i>0: 
                prefix[i] = prefix[i-1] * nums[i-1] 
            returnnums [i] = prefix[i] * suffix[i]
        
        
    
        return returnnums 
            

        