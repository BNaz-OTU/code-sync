class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        output = ""

        for val in s:
            if (len(stack) == 0):
                stack.append(val)
                continue
            elif (stack[-1] == val):
                stack.pop()
            else:
                stack.append(val)
        
        for val in stack:
            output += val

        return output