class Solution:
    def partition(self, s: str) -> list[list[str]]:
        final = []
        part = []

        def dfs(idx):
            if (idx >= len(s)):
                final.append(part.copy())
                return
            
            for j in range(idx, len(s)):
                if self.isPali(s, idx, j):
                    part.append(s[idx:j + 1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return final

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True