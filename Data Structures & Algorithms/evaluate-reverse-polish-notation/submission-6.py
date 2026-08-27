class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        int1 = 1
        int2 = 0
        int3 = 0
        for i in tokens:
            if i not in ['-','+','*','/']:
                stack.append(i)
            else:
                int1 = int(stack.pop())
                int2 = int(stack.pop())
                if i == "+":
                    int3 = int1+int2
                elif i=="-":
                    int3 = int2-int1
                elif i=="*":
                    int3= int1*int2
                elif i=="/":
                    int3 = int2/int1
                print(int3)

                stack.append(int3)
        return int(stack.pop())
                