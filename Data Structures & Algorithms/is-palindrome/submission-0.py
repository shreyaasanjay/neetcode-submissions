class Solution:
    def isPalindrome(self, s: str) -> bool:
        #easiest way to reverse a string: string splicing
        #filter s so that it only include alphanumeric characters
        filtered_s = ""
        for i in range (len(s)):
            if s[i].isalnum():
                filtered_s += s[i].lower()
        new_s = filtered_s[::-1]
        if new_s==filtered_s:
            return True
        
        return False
        