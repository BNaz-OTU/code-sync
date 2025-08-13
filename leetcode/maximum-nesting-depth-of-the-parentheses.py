class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxCount = 0

        for bracket in s:
            if (bracket == '('):
                stack.append(bracket)
            elif (bracket == ')'):
                stack.pop()
            
            if (len(stack) > maxCount):
                maxCount = len(stack)
        
        return maxCount