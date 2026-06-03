class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []

        def dfs(path, idx):
            if (sum(path)> target or idx >= len(candidates)):
                return
            
            if (sum(path)== target):
                if (path not in final):
                    final.append(path.copy())

                return
            
            path.append(candidates[idx])
            dfs(path, idx)      # USE CASE 1: Same number

            path.pop()
            dfs(path, idx + 1)  # USE CASE 2: Don't add number
        
        dfs([], 0)
        return final