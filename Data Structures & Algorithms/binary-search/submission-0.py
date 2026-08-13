class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0;
        right = len(nums) -1
        print(right)
        mid = int ((left+right)/2)
        print(mid)
        while left<right or left==right:
            mid = int((left+right)/2)
            if(target<nums[mid]):
                right = mid-1
                print(right)
        
            elif (target > nums[mid]):
                left = mid+1
                print(left)

            elif target ==nums[mid]:
                return mid
        return -1