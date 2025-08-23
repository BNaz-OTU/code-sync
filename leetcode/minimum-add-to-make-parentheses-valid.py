class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for val in s:
            if (len(stack) > 0 and val == ')' and stack[-1] == '('):
                stack.pop()
            else:
                stack.append(val)
        
        return len(stack)