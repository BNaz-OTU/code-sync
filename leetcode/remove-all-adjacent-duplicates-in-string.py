class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for val in s:
            if (len(stack) > 0 and stack[-1] == val):
                stack.pop()
            else:
                stack.append(val)
        
        return "".join(stack)