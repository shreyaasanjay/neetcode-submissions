class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxval = 0
        hashstring = {}

        #each time we check left<=right:
        #we make a new hashtable and we want to add all the charcers int he substring to the hash table, after doing this for that substring we want to check that there is k enough space to make all of that substring one character, if there is, then we store the length of the character in max value and increase right by 1 and do the process again

        #get hashtable for that specific substring
        while left<len(s) and right<len(s):
            
            hashstring[s[right]] = hashstring.get(s[right],0) + 1

        #compare if total length of substring - max frequency is less than k if yes, then add another to the substring
            if hashstring and ((right-left+1) - max(hashstring.values())) <= k:
                    if (right-left+1)>maxval:
                        maxval = right-left+1
                    right = right+1
            else:
                hashstring[s[left]] = hashstring[s[left]]-1
                left=left+1
                right = right+1
        return maxval