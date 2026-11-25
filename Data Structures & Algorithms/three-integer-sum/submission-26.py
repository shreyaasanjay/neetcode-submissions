class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #common follow ups:
        #is the array sorted
        #zero answer, if theres no triples
        #empty array
        #ok this solution was more of brute force (sol 1)
        #this solution has the correct time complexity

        nums.sort()
        print(nums)
        #THIS IS WHY WE CAN SORT BC WE DONT CARE ABOUT THE INDEXES OMG SO THEY CAN CHANGE
        #print(nums)

        left = 0
        right = 0
        target = 0
        result =[]
        
        for i in range(len(nums)):
            curr = nums[i]
            #ok so if curr is positive, there is no way values after it (greater than curr) can sum to values smaller than curr so we break
            if curr>0:
                break
            
            target = 0-curr
            left = i+1
            right = len(nums)-1
        #because if theres multiple solutions for one i, they should be found in the same round/iteration of i
            if i>0 and nums[i]==nums[i-1]:
                    print("skipping" + str(i))
                    i+=1
                    continue

            while left<right:
                #print("before")
                #print(nums[i], nums[left], nums[right])
                #print(i,left,right)
               
                if nums[left] + nums[right]<target:
                    left+=1
                elif nums[left] + nums[right]>target:
                    right-=1
                
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                
                    while left>0 and left<len(nums)-1 and nums[left]==nums[left-1]:
                        #print("found left duplicate")
                        left+=1
                        
                #     if right>0 and nums[right] == nums[right-1]:
                # #     print("found right duplicate")
                #         right-=1
                    
                #print("after")
                #print(i,left,right)
                #print(nums[i], nums[left], nums[right])
                    
        



        return result