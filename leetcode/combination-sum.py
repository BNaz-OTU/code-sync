class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []

        def dfs(temp, idx):
            if (idx >= len(candidates) or sum(temp) > target):
                return
            
            if (sum(temp) == target):
                final.append(temp.copy())
                return
            
            temp.append(candidates[idx])
            dfs(temp, idx)

            temp.pop()
            dfs(temp, idx + 1)
            
        dfs([], 0)
        return final