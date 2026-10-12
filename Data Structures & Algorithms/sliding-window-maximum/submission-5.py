import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #ok strat is to use a heap
        #since python does auto min heap, we are going to multiply the values by -1 when we add to heap and then get the max value each time 
        numbers = []
        for i in range(len(nums)):
            nums[i] = nums[i]* -1
            nums[i] = (nums[i],i)
        #print(nums)
        for j in range(0,k):
            numbers.append(nums[j])

        heapq.heapify(numbers)
        result = [-1 * numbers[0][0]]
        
        i = k
        while i<len(nums):
            heapq.heappush(numbers, nums[i])
            #print(numbers)
            while numbers[0][1]<=i-k:
                heapq.heappop(numbers)
            #print(numbers)
            result.append(-1 * numbers[0][0])
            i+=1
        
        return result




