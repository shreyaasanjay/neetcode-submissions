class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #common follow ups:
        #is the array sorted
        #zero answer, if theres no triples
        #empty array

        nums.sort()
        #THIS IS WHY WE CAN SORT BC WE DONT CARE ABOUT THE INDEXES OMG SO THEY CAN CHANGE
        #print(nums)

        left = 0
        right = 0
        target = 0
        result =[]
        match = []
        for i in range(len(nums)):
            target = 0-nums[i]
            left = i +1
            right = len(nums)-1

            while left<right:
                if nums[left]+nums[right]<target:
                    left+=1
                elif nums[left]+nums[right]>target:
                    right-=1
                else:
                    match = [nums[i], nums[left], nums[right]]
                    match.sort()
                    if match not in result:
                        result.append([nums[i], nums[left], nums[right]])
                    left+=1
        



        return result