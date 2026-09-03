class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        def dfs(left, right, brackets):
            if (left == n and right == n):
                final.append(brackets)
                return
            
            if (left < n):
                dfs(left + 1, right, brackets + "(")
            
            if (right < left):
                dfs(left, right + 1, brackets + ")")

        dfs(0, 0, "")
        return final