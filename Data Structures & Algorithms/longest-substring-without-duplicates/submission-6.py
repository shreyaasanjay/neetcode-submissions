class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ''
        counts = 0;
        for i in range(len(s)):
            while s[i] in string:
                string = string[1:]
            string = string + s[i]
            if len(string)>counts:
                counts = len(string)
    
        return counts
            
      #idea:
            