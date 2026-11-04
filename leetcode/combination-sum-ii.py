class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        final = []
        temp = []

        def dfs(idx):
            if (idx <= len(candidates) and sum(temp) == target):
                final.append(temp.copy())
                return 
            
            if (idx >= len(candidates) or sum(temp) > target):
                return
            
            temp.append(candidates[idx])
            dfs(idx + 1)

            count = idx
            while (count < len(candidates) and candidates[idx] == candidates[count]):
                count += 1
                
            temp.pop()
            dfs(count)
        
        dfs(0)
        return final