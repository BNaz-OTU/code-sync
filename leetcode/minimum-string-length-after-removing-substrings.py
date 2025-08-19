class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for val in s:
            if (
                (val == 'B' and len(stack) != 0 and stack[-1] == 'A') or 
                (val == 'D' and len(stack) != 0 and stack[-1] == 'C')
                ):

                stack.pop()
            else:
                stack.append(val)
        
        return len(stack)