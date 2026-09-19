class Solution:
    #interview with ridgeline
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        result = [1] * length
        prefix = [1] * length
        suffix = [1]* length

        for i in range(len(nums)):
            if i>0:
                prefix[i] = prefix[i-1] * nums[i-1]
      

        for i in reversed(range(len(nums))):
            if i<len(nums)-1:
                suffix[i] = suffix[i+1] * nums[i+1]
       
        for i in range(length):
            result[i] = prefix[i] * suffix[i]
        
        return result


        
       
        