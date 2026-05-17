class Solution:
    def isValid(self, s: str) -> bool:
        OPEN_BRACKET = ["(", "{", "["]
        stack = []

        for bracket in s:
            if (bracket in OPEN_BRACKET):
                stack.append(bracket)
            
            elif ((len(stack) > 0 and stack[-1] == "(" and bracket == ")") or 
                  (len(stack) > 0 and stack[-1] == "[" and bracket == "]") or 
                  (len(stack) > 0 and stack[-1] == "{" and bracket == "}")):
                stack.pop()
            
            else:
                return False
        
        return len(stack) == 0