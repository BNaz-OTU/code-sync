class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        final = []
        letters = "abc"

        def dfs(text):
            if (len(text) == n):
                final.append(text)
                return

            for letter in letters:
                if (len(text) < n and (text == "" or text[-1] != letter)):
                    dfs(text + letter)
        
        dfs("")

        if (len(final) < k):
            return ""
        else:
            return final[k - 1]