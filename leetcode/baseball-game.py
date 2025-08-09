class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            print(op, ':', stack)
            try:
                if (int(op)):
                    stack.append(int(op))

            except ValueError:
                if (op == 'C'):
                    stack.pop()
                elif (op == 'D'):
                    stack.append(stack[-1] * 2)
                elif (op == '+'):
                    stack.append(stack[-1] + stack[-2])
                    
        print(stack)
        return sum(stack)