class Solution:
    def isValid(self, s: str) -> bool:
        open_set = {"(", "{", "["}
        open_b = []

        for bracket in s:
            if bracket in open_set:
                open_b.append(bracket)
            
            elif (len(open_b) > 0 and bracket == ")" and open_b[-1] == "("):
                open_b.pop()
            
            elif (len(open_b) > 0 and bracket == "}" and open_b[-1] == "{"):
                open_b.pop()
            
            elif (len(open_b) > 0 and bracket == "]" and open_b[-1] == "["):
                open_b.pop()
            
            else:
                return False
        
        return True if len(open_b) == 0 else False