class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(i)
            else:
                if i == "+":
                    result = int(stack[-1]) + int(stack[-2])
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif i=='-':
                    result = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif i=='*':
                    result = int(stack[-1]) * int(stack[-2])
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif i=='/':
                    result = int(int(stack[-2])/int(stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                print(result)
                
        print(stack)
        return int(stack[0])