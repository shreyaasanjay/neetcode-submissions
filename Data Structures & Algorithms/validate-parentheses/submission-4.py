class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) %2 ==1:
            return False
        for i in range(len(s)):
            #if s[i] == "(" or "[" or "{":
            #this is wrong since "[" means true
            if s[i] in "[{(":
                stack.append(s[i])
            if len(stack)==0:
                return False
            if s[i] == ")":
                if stack[-1]=="(":
                    stack.pop()
                else:
                    return False
            if s[i] == "]":
                if stack[-1]=="[":
                    stack.pop()
                else:
                    return False
            if s[i] == "}":
                if stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            print(stack)
        if len(stack)==0:
            return True
        else:
            return False
        
    """
        reverse_s = s[::-1]
        reverses= list(reverse_s)
        for i in range(len(reverse_s)):
         #instead of doing this, you can use the python "replace" method, ok maybe not
            if reverses[i]=="[":
                reverses[i] = "]"
            elif (reverses[i]=="]") :
                reverses[i] = "["
            elif reverses[i]=="(":
                reverses[i] = ")"
            elif reverses[i]==")":
                reverses[i] = "("
            elif reverses[i]=="{":
                reverses[i] = "}"
            elif reverses[i]=="}":
                reverses[i] = "{"
        print(reverses)
        #join is used to convert list to string
        reverse_s = ''.join(reverses)

        if s==reverse_s:
            return True
        return False
     """
    