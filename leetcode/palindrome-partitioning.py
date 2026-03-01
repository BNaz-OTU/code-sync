class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # USED SOLN: https://www.youtube.com/watch?v=3jvWodd7ht0
        res = []
        part = []

        def dfs(idx):
            if (idx >= len(s)):
                res.append(part.copy())
                return
            
            for jdx in range(idx, len(s)):
                if (self.isPali(s, idx, jdx)):
                    part.append(s[idx:jdx + 1])
                    dfs(jdx + 1)
                    part.pop()
        
        dfs(0)
        return res

    def isPali(self, s, left, right):
        while left < right:
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True