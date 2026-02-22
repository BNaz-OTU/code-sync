class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        subset = []

        def dfs(idx, subset):
            if (idx >= len(nums)):
                final.append(subset.copy())
                return
            
            # Add Number
            subset.append(nums[idx])
            dfs(idx + 1, subset)

            # Don't Add Number
            subset.pop()
            dfs(idx + 1, subset)

        dfs(0, subset)
        return final