class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        consec = [nums[0]]
        maxlength = 0

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                consec.append(nums[i+1])
            elif nums[i+1] == nums[i]:
                continue
            else:
                maxlength = max(maxlength, len(consec))
                consec = [nums[i]]

        maxlength = max(maxlength, len(consec))
        return maxlength



