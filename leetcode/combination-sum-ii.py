class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # USED SOLN: https://www.youtube.com/watch?v=FOyRpNUSFeA&t=38s
        final = []
        subset = []
        candidates.sort()

        def dfs(idx, subset):
            if (sum(subset) == target):
                final.append(subset.copy())
                return 

            if (sum(subset) > target or idx >= len(candidates)):
                return
            
            subset.append(candidates[idx])
            dfs(idx + 1, subset)
            subset.pop()

            # Skip candidate
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1

            dfs(idx + 1, subset)

        dfs(0, subset)
        return final