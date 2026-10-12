class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #basically its simple binary search, first u have a left, mid and right

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[l] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Search left
                else:
                    l = mid + 1
            else:
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Search right
                else:
                    r = mid - 1

        return -1

        # 1234
        # 561234

        # 1234567

        # 45670123

        # left = 0
        # right = len(nums)-1
        # mid = (left+right)//2

        # #if mid>=left then we look at the left side then we know mid is in the left sorted part,
        # #if if mid<left, we are in right sorted array

        # while left<=right:
        #     mid = (left+right)//2
            
            
        #     if nums[mid]==target:
        #         return mid

        #     #mid is in left sorted portion
            
        #     if nums[mid]>=nums[left]:
        #         #if target is greater than mid, we know its in the right portion of mid but also in the left portion of the whole array
        #         if nums[left]<=target<nums[mid]:
        #             left=mid+1
        #     #if target is less than nums[mid]
        #         else:
        #             right = mid-1
                    
        #     #if mid is in the right sorted portion of the array
        #     else:
        #         #if target is less than mid but mid is in the right sorted array then right still goes to the right of mid since target cannot be to the right of mid (everything o the right of mid )
        #         if nums[mid]<target<=nums[right]:
        #             right = mid-1
        #         else:
        #             right = mid-1
        # return -1
                    



        
        
        
# /* OLD IMPLEMENTATION
#         #first find the cut
#     /*cut = 0
#         for i in range(len(nums)-1):
#             if nums[i] > nums[i+1]:
#                 cut = i+1
#                 break
#         print(cut)

#         #so if the target is greater than pivot we know its to the right and if target is less than pivot we know its to the left 

#         left = 0
#         right = len(nums)-1

#         if target>cut:
#             left = cut + 1
        
#         elif target<cut:
#             right = cut-1
#         else:
#             return cut
#         print(left,right)
#         mid = 0
#         #simple binary search
#         while left<right:
#             mid = (left+right)/2
#             if target<mid:
#                 right = mid+1
#             elif target>mid:
#                 left = mid+1
#             else:
#                 return int(mid)
#         return -1
#     */




