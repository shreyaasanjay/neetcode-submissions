class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       left = 0
       right = len(nums)-1
       differences = []

       for i in range(len(nums)):
            difference = target-nums[i]
            if nums[i] in differences:
                return [nums.index(difference), i]
            else:
                differences.append(difference)