import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        heapq.heapify(stones)
        print(stones)
        val = 0
        
        while len(stones)>1:
            print(stones)
            if stones[-1]==stones[-2]:
                val = stones[-1]
                stones.remove(val)
                stones.remove(val)
                heapq.heapify(stones)
            else:
                val = abs(stones[-1]-stones[-2])
                stones[-1] = val
                stones.remove(stones[-2])
                heapq.heapify(stones)
        if len(stones)==0:
            return 0
        else:
            return stones[0]


        
        
        
        return 9