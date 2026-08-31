class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []

        def dfs(subset, idx):
            if (idx == len(nums)):
                final.append(subset.copy())
                return
            
            subset.append(nums[idx])
            dfs(subset, idx + 1)

            subset.pop()
            dfs(subset, idx + 1)
        
        dfs([], 0)
        return final