class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #implemented with hashmap but better like O(n)
        s_stringhash= {}
        t_stringhash = {}
        for char in s:
           s_stringhash[char]=s_stringhash.get(char,0) + 1
        
        for char in t:
            t_stringhash[char] = t_stringhash.get(char,0)+1
        
        
        if s_stringhash==t_stringhash:
            return True
        else:
            return False