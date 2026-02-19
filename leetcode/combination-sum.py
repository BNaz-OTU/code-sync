class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # USED SOLN: https://www.youtube.com/watch?v=GBKI9VSKdGg
        
        final = []
        current = []

        def dfs(idx, current):

            if (sum(current) == target):
                final.append(current.copy())
                return

            if (idx >= len(candidates) or sum(current) > target):
                return
            
            current.append(candidates[idx])
            dfs(idx, current)

            current.pop()
            dfs(idx + 1, current)
        
        dfs(0, current)
        return final