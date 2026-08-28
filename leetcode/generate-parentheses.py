class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []

        def dfs(parenth_str, left, right):
            if (left == n and right == n):
                final.append(parenth_str)
                return 

            if (left < n):
                dfs(parenth_str + "(", left + 1, right)
            
            if (right < left):
                dfs(parenth_str + ")", left, right + 1)
        
        dfs("", 0, 0)
        return final