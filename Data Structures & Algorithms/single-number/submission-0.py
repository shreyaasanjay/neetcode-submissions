class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        freq = {}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=0

        for i in freq:
            if freq[i]==0:
                return i