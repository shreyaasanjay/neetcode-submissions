class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap, two identify arrays 

        words = {}
        freq = {}
        result = []

        for i in strs:
            for m in i:
                if m not in freq:
                    freq[m]=1
                else:
                    freq[m]+=1
            if tuple(sorted(freq.items())) not in words:
                words[tuple(sorted(freq.items()))] = [i]
            
            else:
                words[tuple(sorted(freq.items()))].append(i)
            freq = {}
        
        
        for i in words:
            result.append(words[i])

        return result