class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        sort_cand = sorted(candidates)

        def dfs(path, idx):
            if (sum(path) == target and path not in final):
                # print(path, sorted(path))
                final.append(path.copy())
                return

            if (sum(path) > target or idx >= len(sort_cand)):
                return
            
            path.append(sort_cand[idx])
            dfs(path, idx + 1)

            path.pop()
            count = idx
            while count < len(sort_cand) and sort_cand[idx] == sort_cand[count]:
                count += 1

            dfs(path, count)
        
        dfs([], 0)
        return final