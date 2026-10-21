class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #use the basic heap solution 

        negnums = [0] * len(nums)
        for i in range(len(nums)):
            negnums[i] = -1 * nums[i]
        heapq.heapify(negnums)
        #print(negnums)


        for i in range(k-1):
            heapq.heappop(negnums)


        return negnums[0] * -1