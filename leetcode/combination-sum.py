class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        final = []
        temp = []

        def dfs(idx):
            if (idx <= len(candidates) and sum(temp) == target):
                final.append(temp.copy())
                return
            
            if (idx >= len(candidates) or sum(temp) > target):
                return

            temp.append(candidates[idx])
            dfs(idx)
            temp.pop()
            dfs(idx + 1)
        
        dfs(0)
        return final