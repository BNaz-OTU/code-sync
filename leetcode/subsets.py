class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []

        def dfs(idx, subset):
            if (idx == len(nums)):
                final.append(subset.copy())
                return
            
            subset.append(nums[idx])
            dfs(idx + 1, subset)

            subset.pop()
            dfs(idx + 1, subset)
        
        dfs(0, [])
        return final