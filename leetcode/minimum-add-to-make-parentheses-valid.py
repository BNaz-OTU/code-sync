class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bracketStack = []

        for val in s:
            if (val == "("):
                bracketStack.append(val)
            elif (len(bracketStack) > 0 and bracketStack[-1] == '(' and val == ')'):
                bracketStack.pop()
            else:
                bracketStack.append(val)
        
        return len(bracketStack)