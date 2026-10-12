class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        #not rlly sliding window
        #store all in freq haqsh table
        #store an array w indexes that they showed up

        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = [i]
            else:
                freq[nums[i]].append(i)
        print(freq)
        j=0
        for i in freq:
            if len(freq[i])>=2:
                while j<len(freq[i])-1:
                    if freq[i][j+1]-freq[i][j]<=k:
                        return True
                    j+=1
        
        return False

