class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for val in s: 
            if (len(stack) > 0 and ord(val) < 97 and ((ord(val) + 32) == ord(stack[-1]))):
                stack.pop()

            elif (len(stack) > 0 and ord(val) >= 97 and ((ord(val) - 32) == ord(stack[-1]))):
                stack.pop()
            
            else:
                stack.append(val)
        
        return "".join(stack)