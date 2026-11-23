class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #okay tried two pointers but scrap this since its not sorted so we cant assume that increasing the left pointer will result in a greater sum
    #use a hashmap since we know that look up is o(1) and store its index


        seen = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                return [seen[difference], i]
            else:
                seen[nums[i]] = i
                

        
        
        # #since we want an o(n) time, we only want to look at 
        # #each value once

        # left = 0
        # right = len(nums)-1
        # nums.sort

        # while left<=right:
        #     if abs(nums[left]+nums[right])>abs(target):
        #         right-=1

        #     elif abs(nums[left]+nums[right])<abs(target):
        #         left+=1
            
        #     else:
        #         return [left, right]