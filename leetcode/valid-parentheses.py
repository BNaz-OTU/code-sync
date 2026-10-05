class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBracket = {"(", "{", "["}

        for bracket in s:
            if bracket in openBracket:
                stack.append(bracket)
            
            elif (len(stack) > 0 and bracket == "]" and stack[-1] == "["):
                stack.pop()
            
            elif (len(stack) > 0 and bracket == ")" and stack[-1] == "("):
                stack.pop()
            
            elif (len(stack) > 0 and bracket == "}" and stack[-1] == "{"):
                stack.pop()
            
            else:
                return False
        
        return True if len(stack) == 0 else False