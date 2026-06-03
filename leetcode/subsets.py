class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []

        def dfs(path, idx):
            if (idx >= len(nums)):
                final.append(path.copy())
                return

            path.append(nums[idx])
            dfs(path, idx + 1)
            path.pop()
            dfs(path, idx + 1)
        
        dfs([], 0)
        return final