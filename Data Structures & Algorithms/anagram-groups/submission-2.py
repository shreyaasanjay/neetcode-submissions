class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #main idea:
        #get character counts for each string in strs
        #then convert it to a tuple because it must be hashable (read this)
        #anogther thing nis that append doesnt work for dicts, just add 
       
        string_hash = {}
        returnstrings = []
        for s in strs:
            character_count = {}
            for char in s:
                character_count[char] = character_count.get(char,0)+1
            string_hash[tuple(sorted(character_count.items()))] = string_hash.get(tuple(sorted(character_count.items())),[]) + [s]
        
        for s in string_hash:
            returnstrings.append(string_hash[s])
        
        return returnstrings




