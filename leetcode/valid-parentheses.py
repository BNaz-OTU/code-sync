class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        OPEN_BRACKET = ["(", "[", "{"]

        for bracket in s:
            if bracket in OPEN_BRACKET:
                stack.append(bracket)
            
            elif (len(stack) > 0 and bracket == ")" and stack[-1] == "("):
                stack.pop()
            
            elif (len(stack) > 0 and bracket == "]" and stack[-1] == "["):
                stack.pop()
            
            elif (len(stack) > 0 and bracket == "}" and stack[-1] == "{"):
                stack.pop()
            
            else:
                return False
        
        return len(stack) == 0