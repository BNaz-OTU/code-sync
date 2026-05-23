class Solution:
    def isValid(self, s: str) -> bool:
        OPEN_B = {"(", "[", "{"}
        stack = []

        for bracket in s:
            if (bracket in OPEN_B):
                stack.append(bracket)
            
            elif (len(stack) > 0 and stack[-1] == "(" and bracket == ")"):
                stack.pop()
            
            elif (len(stack) > 0 and stack[-1] == "[" and bracket == "]"):
                stack.pop()
            
            elif (len(stack) > 0 and stack[-1] == "{" and bracket == "}"):
                stack.pop()
            
            else:
                return False
        
        return len(stack) == 0