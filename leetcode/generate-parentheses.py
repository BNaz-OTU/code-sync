class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        
        def dfs(brackets, left, right):
            if (left >= n and right >= n):
                final.append(brackets)
            
            if (left < n):
                dfs(brackets + "(", left + 1, right)
            
            if (left > right):
                dfs(brackets + ")", left, right + 1)
        
        dfs("", 0, 0)
        return final