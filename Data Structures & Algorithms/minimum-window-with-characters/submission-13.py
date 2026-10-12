class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        

        #create need freq table for characters in t
        need = {}
        for i in t:
            if i not in need:
                need[i]=1
            else:
                need[i]+=1
        
        
        #sliding window approach
        left = 0
        right = 0

        #create have hash table - what we already see
        have = {}
        for i in t:
            if i not in have:
                have[i]=0
        
        
        havenum = 0
        neednum = len(need)
        minsub = {}

        while right<len(s) or havenum==neednum:
            if havenum==neednum:
                minsub[(left,right)] = right-left
                if s[left] in have:
                    have[s[left]]-=1
                    if have[s[left]]<need[s[left]]:
                        havenum-=1
                left+=1
            else:
                if s[right] in have:
                    have[s[right]]+=1
                    if have[s[right]]==need[s[right]]:
                        havenum+=1
                right+=1
            
        if minsub == {}:
            return ""

        substring = min(minsub, key=minsub.get)  
        return s[substring[0]:substring[1]]
        

        


