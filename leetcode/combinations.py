class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        final = []

        def dfs(idx, subset):
            if (len(subset) == k):
                final.append(subset.copy())
                return
            
            for jdx in range(idx, n):
                subset.append(jdx + 1)
                dfs(jdx + 1, subset)
                subset.pop()
                    
        dfs(0, [])
        return final