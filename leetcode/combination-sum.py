class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []

        def dfs(path, idx):
            if (sum(path) > target or idx >= len(candidates)):
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