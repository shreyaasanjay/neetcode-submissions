import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.k = k
        i=len(nums)-1
        nums.sort()
        while i > (len(nums) - 1 - k) and i>-1:
            heapq.heappush(self.minheap,nums[i])
            i = i-1
        print(self.minheap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        while len(self.minheap)> self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
        
                        
    


        
