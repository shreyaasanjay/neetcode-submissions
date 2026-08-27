class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #implemented with hashmap
        s_stringhash= {}
        t_stringhash = {}
        for char in s:
            if char not in s_stringhash:
                numchar = 0
                for newchar in s:
                    if char==newchar:
                        numchar+=1
                s_stringhash[char] = numchar
        
        for char in t:
            if char not in t_stringhash:
                numchar = 0
                for newchar in t:
                    if char==newchar:
                        numchar+=1
                t_stringhash[char] = numchar
        
        print(s_stringhash)
        print(t_stringhash)
        if s_stringhash==t_stringhash:
            return True
        else:
            return False