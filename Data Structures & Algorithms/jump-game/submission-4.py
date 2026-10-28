class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #trick: you dont have to jump the whole way
        curpos = 0
        nextpos = 0
        jump = 0
        maxindex = 0
        
        for i in range(len(nums)):
            if i<=maxindex:
                maxindex = max(maxindex, i+nums[i])
                print(maxindex, i, nums[i])

            else:
                return False

        return True

        #     while nums[i]<maxindex
        #     if i==nums
        #     maxindex = max(maxindex, maxindex+nums[0])
            


        #     if curpos>=len(nums):
        #         break
        #     elif nums[curpos]==0:
        #         break

        
        # if curpos<len(nums)-1:
        #     return False
        # return True

