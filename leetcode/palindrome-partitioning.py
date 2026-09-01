class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final = []
        temp = []

        def dfs(idx):
            if (idx >= len(s)):
                final.append(temp.copy())
                return

            for jdx in range(idx, len(s)):
                if self.isPali(s, idx, jdx):
                    temp.append(s[idx:jdx + 1])
                    dfs(jdx + 1)
                    temp.pop()
        
        dfs(0)
        return final


    def isPali(self, s, left, right):
        while left < right:
            if (s[left] != s[right]):
                return False
            
            left += 1
            right -= 1
        
        return True