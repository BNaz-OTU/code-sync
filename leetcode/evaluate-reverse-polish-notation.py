class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            try:
                if (int(tok) or tok == '0'):
                    stack.append(int(tok))

            except ValueError:
                operand_1, operand_2 = stack.pop(), stack.pop()

                if (tok == '+'):
                    new_val = operand_2 + operand_1
                    # print(operand_1, tok, operand_2)
                elif (tok == '-'):
                    new_val = operand_2 - operand_1
                    # print(operand_1, tok, operand_2)
                elif (tok == '/'):
                    # This will help truncate to 1 decimal by using both 'int' and
                    # regular division operation, (the '//' integer divison operation
                    # will round weird with negative numbers)
                    new_val = int(operand_2 / operand_1) 

                    # print(operand_2, tok, operand_1)
                    # print(new_val)
                else:
                    new_val = operand_1 * operand_2
                    # print(operand_1, tok, operand_2)
                
                stack.append(new_val)
        
        return stack[-1]