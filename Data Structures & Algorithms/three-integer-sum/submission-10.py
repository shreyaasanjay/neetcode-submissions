class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        right = 0
        target = 0
        match = []
        result = []
        nums.sort()

        for i in range(len(nums)):
            target = -1 * nums[i]
            left=i+1
            right = len(nums)-1
            while left<right and left!=i and right!=i:
                if nums[left]+nums[right]>target:
                    right = right-1
                elif nums[left]+nums[right]<target:
                    left= left+1
                else:
                    match = [target*-1,nums[left], nums[right]]
                    match.sort()
                    if match not in result:
                        result.append(match)
                    right = right-1
                    left = left+1
        return result

