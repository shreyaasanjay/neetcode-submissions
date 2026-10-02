class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = ""
        length = ""
        j = 0
        for i in strs:
            length = str(len(i))
            j = len(length)
            while j<3:
                length = "0" + length
                j+=1
            result+=str(length)
            result+=(i)
        print(result)
        
        return result


    def decode(self, s: str) -> List[str]:
        #so my thought process is we want to seperate the words by length
        #so when we get to a number, we can store it as j 
        #and then we read the next j characters and append those to a string 
        #and then append the string to result
        
        length = 0
        result = []
        string = ""
        j = 1
        nums = 0
        #find out how many numbers there are:
        for i in s:
            if i.isdigit():
                nums +=1
        
        while len(s)!=0:
            length = int(s[:3])
            s=s[3:]
            for i in range(length):
                string += s[i]
            s=s[length:]
        
            result.append(string)
            string = ""
        
        return result
