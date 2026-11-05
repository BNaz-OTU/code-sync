class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        final = []
        
        def dfs(left, right, bracket):
            if (left == n and right == n):
                final.append(bracket)
                return
            
            if (left > right):
                # bracket += ")"
                dfs(left, right + 1, bracket + ")")
                # bracket = bracket[:-1]
            
            if (left < n):
                # bracket += "("
                dfs(left + 1, right, bracket + "(") 
                # bracket = bracket[:-1]
        
        dfs(0, 0, "")
        return final