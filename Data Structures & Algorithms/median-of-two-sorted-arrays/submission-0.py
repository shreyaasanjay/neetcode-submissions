class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = nums1
        for i in nums2:
            result.append(i)
        result.sort()
        if len(result)%2==1:
            return result[len(result)//2]
        else:
            return (result[len(result)//2]+result[(len(result)//2)-1])/2