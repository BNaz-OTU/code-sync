import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if (token in "+-/*"):
                print(stack[-2], token, stack[-1])

            if (token == "+"):
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(str(op2 + op1))
            
            elif (token == "-"):
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(str(op2 - op1))
            
            elif (token == "*"):
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(str(op2 * op1))
            
            elif (token == "/"):
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                val = int(op2 / op1)
                stack.append(str(val))
        
            else:
                stack.append(token)

        return int(stack[0])