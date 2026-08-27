class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #still used chat but I learned that there is a python dictionary function to find key with the max value associated with it
        numfreq = {}
        maxfreq = 0
        val = 0
        returnnums = []
        for i in nums:
            numfreq[i] = numfreq.get(i,0) + 1
        
        while k>0:
            val = max(numfreq, key=numfreq.get)
            returnnums.append(val)
            del numfreq[val]
            k = k-1
        return returnnums
