class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #first do the case that not all the letters in string s1 are in s2
        firstpass = False
        for i in s1:
            if i in s2:
                firstpass = True
        if firstpass == False:
            return False
        
        #use a sliding window with len s1 and for each window check if the freq hashmap is equal to s1 freq
        freqs1 = {}

        for i in s1:
            if i not in freqs1:
                freqs1[i]=1
            else:
                freqs1[i]+=1
       
        freqs2 = {}
        sets2 = []
        #idea for sliding window - make a new array with three elements and make a hashmap for 
        #that array, if that hashmap is equal to freqs1 return true  
    
        
        sets2 = []
        #create first sets2 array:
        for i in range(0,len(s1)-1):
            sets2.append(s2[i])


        for i in range(0, len(s2)-len(s1)+1):
            freqs2={}
            sets2.append(s2[i+(len(s1)-1)])
           
            for i in sets2:
                if i not in freqs2:
                    freqs2[i]=1
                else:
                    freqs2[i]+=1
            print(freqs2)
            if freqs2==freqs1:
                return True
            del sets2[0]
        return False




                
                
        return True