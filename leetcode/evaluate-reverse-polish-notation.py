class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                op2 = stack.pop()
                op1 = stack.pop()

                print(op1, token, op2)
                if token == "*":
                    val = int(op1) * int(op2)
                    stack.append(str(val))
                
                elif token == "+":
                    val = int(op1) + int(op2)
                    stack.append(str(val))
                
                elif token == "-":
                    val = int(op1) - int(op2)
                    stack.append(str(val))
                
                else:
                    val = int(int(op1) / int(op2))
                    stack.append(str(val))
            else:
                stack.append(token)
        
        return int(stack[-1])