class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        new_freq = []
        result = []
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i in freq:
            temp = freq[i]
            new_freq.append((temp, i))

        #print(freq)
        new_freq.sort()
        new_freq = new_freq[::-1]
        #print(new_freq)

        top = 0
        while top<k:
            result.append(new_freq[top][1])
            top+=1
        

        return result