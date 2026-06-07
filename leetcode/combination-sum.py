class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        def dfs(path, idx):
            if (idx >= len(candidates) or sum(path) > target):
                return
            
            if (sum(path) == target):
                final.append(path.copy())
                return
            
            path.append(candidates[idx])
            dfs(path, idx)

            path.pop()
            dfs(path, idx + 1)
        
        dfs([], 0)
        return final