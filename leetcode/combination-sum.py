class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        subset = []

        def dfs(idx, subset):
            if (sum(subset) > target or idx >= len(candidates)):
                return
            
            if (sum(subset) == target and subset not in final):
                final.append(subset.copy())
                return 
            
            print(idx, subset)
            
            # Add and continue further in the list
            subset.append(candidates[idx])
            dfs(idx + 1, subset)

            # Don't do anything (Continue with the same number)
            dfs(idx, subset)

            # Don't add but continue further in the list
            subset.pop()
            dfs(idx + 1, subset)

        
        dfs(0, subset)
        return final