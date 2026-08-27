class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #implemented with hashmap but better like O(n)
        s_stringhash= {}
        t_stringhash = {}
        for char in s:
           s_stringhash[char]=s_stringhash.get(char,0) + 1
        
        for char in t:
            if char not in t_stringhash:
                numchar = 0
                for newchar in t:
                    if char==newchar:
                        numchar+=1
                t_stringhash[char] = numchar
        
        
        if s_stringhash==t_stringhash:
            return True
        else:
            return False