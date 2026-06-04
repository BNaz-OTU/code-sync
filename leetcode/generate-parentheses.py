class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        stack = []

        def dfs(n_left, n_right):
            if (n_left == n and n_right == n):
                val = "".join(stack)
                final.append(val)
                return 
            
            if (n > n_left):
                stack.append("(")
                dfs(n_left + 1, n_right)
                stack.pop()

            if (n_left > n_right):
                stack.append(")")
                dfs(n_left, n_right + 1)
                stack.pop()
            
        dfs(0, 0)
        return final