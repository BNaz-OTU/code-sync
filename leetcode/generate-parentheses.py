class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []

        def dfs(text, left, right):
            # print(text)
            if (left == n and right == n):
                final.append(text)
                return
            
            if (left < n):
                dfs(text + "(", left + 1, right)
            
            if (right < left):
                dfs(text + ")", left, right + 1)

        dfs("", 0, 0)
        return final