class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        
        def dfs(brackets, left, right):
            if (left == 0 and right == 0):
                final.append(brackets)
                return
            
            if (left != 0):
                dfs(brackets + "(", left - 1, right)
            
            if (left == 0 or left < right):
                dfs(brackets + ")", left, right - 1)
            
        dfs("", n, n)
        return final