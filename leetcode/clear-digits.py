class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        final = ""

        for char in s:
            if (char.isnumeric()):
                stack.pop()
            else:
                stack.append(char)
        
        for _ in range(len(stack)):
            final += stack.pop()
        
        return final[::-1]