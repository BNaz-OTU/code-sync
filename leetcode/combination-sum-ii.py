class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        candidates.sort()

        def dfs(path, idx):
            if (sum(path) == target):
                final.append(path.copy())
                return

            if (idx >= len(candidates) or sum(path) > target):
                return
        
            path.append(candidates[idx])
            dfs(path, idx + 1)

            count = idx
            while count < len(candidates) and candidates[idx] == candidates[count]:
                count += 1
            
            path.pop()
            dfs(path, count)
        
        dfs([], 0)
        return final