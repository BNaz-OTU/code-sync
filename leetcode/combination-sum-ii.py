class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # USED SOLN: https://www.youtube.com/watch?v=rSA3t6BDDwg&t=93s
        candidates.sort()

        final = []

        def backtrack(cur, pos, target):
            if (target == 0):
                final.append(cur.copy())
            if (target <= 0):
                return 
            
            prev = -1

            for i in range(pos, len(candidates)):
                if (candidates[i] == prev):
                    continue
                
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
        
        backtrack([], 0, target)
        return final